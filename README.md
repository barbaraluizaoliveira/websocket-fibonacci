# Websocket fibonacci server

Este projeto implementa um servidor WebSocket assíncrono utilizando Python e a biblioteca FastAPI. O servidor aceita conexões de múltiplos clientes e oferece funcionalidades como o envio de dados em tempo real (data e hora) e o processamento assíncrono do algoritmo de Fibonacci. Além disso, gerencia os usuários conectados e armazena esses dados em um banco de dados PostgreSQL usando a ORM SQLAlchemy.
<div style="display: inline_block">
  <img align="center" alt="Rafa-Js" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-plain.svg">
  <img align="center" alt="Rafa-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
  <img align="center" alt="Rafa-Csharp" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/sqlalchemy/sqlalchemy-plain.svg">
  <img align="center" alt="Rafa-Csharp" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-plain.svg">
  <img align="center" alt="Rafa-Csharp" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/fastapi/fastapi-plain.svg">
</div>

# Tecnologias Utilizadas
Python: Linguagem de programação principal.

FastAPI: Framework assíncrono para construir APIs.

WebSockets: Protocolo para comunicação bidirecional em tempo real.

SQLAlchemy: ORM para interagir com o banco de dados.

PostgreSQL: Banco de dados relacional utilizado para armazenar dados de usuários conectados.

Docker: Containerização do ambiente de desenvolvimento.

Alembic: Ferramenta para migração de banco de dados (não resolvida completamente).

# Funcionalidades
Conexão via WebSocket: O servidor permite múltiplas conexões WebSocket com clientes e troca dados em tempo real.

Envio de Data Atual: A cada segundo, o servidor envia a data e hora atuais para todos os clientes conectados.

Gestão de Usuários Conectados: O servidor registra os usuários que estão conectados e salva essas informações no banco de dados. O banco de dados é atualizado sempre que um usuário se conecta ou desconecta.

Processamento de Comandos: Quando um cliente envia um número n, o servidor processa o número de Fibonacci e envia o resultado de volta para o cliente.

Docker: O ambiente foi containerizado usando Docker e Docker Compose para orquestrar o banco de dados e a aplicação.

# Estrutura do Projeto
server.py: Implementação do servidor WebSocket.

models/connected_user.py: Modelo do banco de dados para armazenar os usuários conectados.

service.py: Funções auxiliares para salvar e remover usuários conectados do banco.

db.py: Configuração do banco de dados e do SQLAlchemy.

Dockerfile: Arquivo para containerizar a aplicação.

docker-compose.yml: Arquivo opcional para orquestrar a aplicação e o banco de dados PostgreSQL.

# Como Rodar o Projeto
Requisitos
Docker e Docker Compose instalados.

Python 3.7+.

Passos
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/websocket-fibonacci-server.git
cd websocket-fibonacci-server
Construa e inicie os containers Docker:

bash
Copiar
Editar
docker-compose up --build
Isso irá iniciar tanto o servidor da aplicação quanto o banco de dados PostgreSQL.

O servidor WebSocket estará disponível na porta 8000. Você pode usar um cliente WebSocket para se conectar e testar.

# Problemas Conhecidos
Problemas com Alembic: Durante a implementação das migrations com Alembic, encontrei vários erros ao tentar gerar as migrations e popular o banco de dados. Não consegui resolver completamente essa parte, então as migrations não foram configuradas corretamente.

# Como Testar
Após iniciar o servidor, você pode se conectar ao WebSocket utilizando um cliente WebSocket, como o Insomnia. No Insomnia, basta criar uma nova requisição WebSocket, conectar ao servidor na URL ws://localhost:8000/{username}, enviar um número n e o servidor retornará o número de Fibonacci correspondente.

# Contribuições
Sinta-se à vontade para contribuir com o projeto! Se encontrar algum bug ou tiver sugestões de melhorias, crie uma issue ou envie um pull request.
