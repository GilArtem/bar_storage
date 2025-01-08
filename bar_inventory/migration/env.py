from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os

# Загрузка переменных окружения
from dotenv import load_dotenv
load_dotenv()

# Alembic конфигурация
config = context.config

# Установка URL подключения
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    print(f"DATABASE_URL: {DATABASE_URL}")
else:
    raise ValueError("Ошибка: DATABASE_URL не задано")

config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Настройка логирования
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Импорт моделей и метаданных
from app.models.base import Base
from app.models.product import Product  # Убедитесь, что путь правильный
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Запуск миграций в 'offline' режиме."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Запуск миграций в 'online' режиме."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()








































# from logging.config import fileConfig
# from sqlalchemy import engine_from_config, pool
# from alembic import context
# from app.models.base import Base  # Убедитесь, что путь правильный
# import os

# # Load environment variables from .env file
# from dotenv import load_dotenv
# load_dotenv()

# # Alembic configuration
# config = context.config

# # Update the sqlalchemy.url dynamically based on environment variables
# DATABASE_URL = os.getenv("DATABASE_URL")
# config.set_main_option("sqlalchemy.url", DATABASE_URL)

# # print(os.getenv("DATABASE_URL"))

# # Set up logging
# if config.config_file_name is not None:
#     fileConfig(config.config_file_name)

# # Add your model's MetaData for autogenerate support
# # Update target_metadata to reflect your application's models
# target_metadata = Base.metadata

# def run_migrations_offline() -> None:
#     """Run migrations in 'offline' mode."""
#     url = config.get_main_option("sqlalchemy.url")
#     context.configure(
#         url=url,
#         target_metadata=target_metadata,
#         literal_binds=True,
#         dialect_opts={"paramstyle": "named"},
#     )

#     with context.begin_transaction():
#         context.run_migrations()

# def run_migrations_online() -> None:
#     """Run migrations in 'online' mode."""
#     connectable = engine_from_config(
#         config.get_section(config.config_ini_section, {}),
#         prefix="sqlalchemy.",
#         poolclass=pool.NullPool,
#     )

#     with connectable.connect() as connection:
#         context.configure(
#             connection=connection,
#             target_metadata=target_metadata
#         )

#         with context.begin_transaction():
#             context.run_migrations()

# if context.is_offline_mode():
#     run_migrations_offline()
# else:
#     run_migrations_online()











# from logging.config import fileConfig

# from sqlalchemy import engine_from_config
# from sqlalchemy import pool

# from alembic import context

# from app.models.base import Base

# from dotenv import load_dotenv
# import os

# load_dotenv()


# # this is the Alembic Config object, which provides
# # access to the values within the .ini file in use.
# config = context.config

# # Interpret the config file for Python logging.
# # This line sets up loggers basically.
# if config.config_file_name is not None:
#     fileConfig(config.config_file_name)

# # изменить sqlalchemy.url
# DATABASE_URL = os.getenv("DATABASE_URL")
# config.set_main_option("sqlalchemy.url", DATABASE_URL)


# # add your model's MetaData object here
# # for 'autogenerate' support
# # from myapp import mymodel
# # target_metadata = mymodel.Base.metadata
# target_metadata = None

# # other values from the config, defined by the needs of env.py,
# # can be acquired:
# # my_important_option = config.get_main_option("my_important_option")
# # ... etc.


# def run_migrations_offline() -> None:
#     """Run migrations in 'offline' mode.

#     This configures the context with just a URL
#     and not an Engine, though an Engine is acceptable
#     here as well.  By skipping the Engine creation
#     we don't even need a DBAPI to be available.

#     Calls to context.execute() here emit the given string to the
#     script output.

#     """
#     url = config.get_main_option("sqlalchemy.url")
#     context.configure(
#         url=url,
#         target_metadata=target_metadata,
#         literal_binds=True,
#         dialect_opts={"paramstyle": "named"},
#     )

#     with context.begin_transaction():
#         context.run_migrations()


# def run_migrations_online() -> None:
#     """Run migrations in 'online' mode.

#     In this scenario we need to create an Engine
#     and associate a connection with the context.

#     """
#     connectable = engine_from_config(
#         config.get_section(config.config_ini_section, {}),
#         prefix="sqlalchemy.",
#         poolclass=pool.NullPool,
#     )

#     with connectable.connect() as connection:
#         context.configure(
#             connection=connection, target_metadata=Base.metadata  # Это укажет Alembic на метаданные наших моделей
#         )

#         with context.begin_transaction():
#             context.run_migrations()


# if context.is_offline_mode():
#     run_migrations_offline()
# else:
#     run_migrations_online()
