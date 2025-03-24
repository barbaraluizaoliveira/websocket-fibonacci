import sys
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import MetaData
from alembic import context
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.models import ConnectedUser  

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = MetaData()

target_metadata = ConnectedUser.metadata  

config.set_section_option("alembic", "sqlalchemy.url", "postgresql://admin_user:S3nh%%40F0rt3%%212025@172.22.0.2:5432/desafio_db")

def run_migrations_offline():
    """Executa migrações no modo offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Executa migrações no modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
