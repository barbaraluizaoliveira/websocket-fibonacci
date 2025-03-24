import asyncio
import websockets
from fastapi import FastAPI, Depends
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.db import get_db, engine
from datetime import datetime, timezone
from app.models.connected_user import ConnectedUser
from app.service import save_user_connected, remove_user_connected
import websockets.exceptions

app = FastAPI()

async def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

async def websocket_handler(websocket, path):
    if not path or path == "/":
        print("Conexão recusada: nome de usuário inválido.")
        return
    
    username = path.strip("/")
    connection_time = datetime.now(timezone.utc)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    try:
        save_user_connected(db, username, connection_time)
        print(f"Usuário {username} conectado às {connection_time}.")
        
        while True:
            await websocket.send(str(datetime.now(timezone.utc)))
            await asyncio.sleep(1)
            message = await websocket.recv()
            n = int(message)
            fib_result = await fibonacci(n)
            await websocket.send(str(fib_result))
    except websockets.exceptions.ConnectionClosed:
        print(f"Usuário {username} desconectado.")
    except Exception as e:
        print(f"Erro no WebSocket: {e}")
    finally:
        remove_user_connected(db, username)
        db.close()

async def main():
    while True:
        try:
            server = await websockets.serve(websocket_handler, "0.0.0.0", 8000)
            print("Servidor WebSocket iniciado na porta 8000.")
            await server.wait_closed()
        except Exception as e:
            print(f"Erro ao iniciar WebSocket: {e}. Tentando novamente em 5 segundos...")
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())
