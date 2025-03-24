import websockets
import asyncio

async def connect_websocket():
    uri = "ws://localhost:8000/someuser"
    async with websockets.connect(uri) as websocket:
        while True:
            msg = await websocket.recv()
            print(f"Data e hora recebida: {msg}")

            n = input("Digite um número para Fibonacci: ")
            await websocket.send(n)
            result = await websocket.recv()
            print(f"Resultado: {result}")

asyncio.run(connect_websocket())
