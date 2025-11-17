from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool


import os
from dotenv import load_dotenv

import app.models.task
import app.models.user

from app.core.config import get_settings
from app.db.base import Base

# =========================================================================
# >> НАЧАЛО ИСПРАВЛЕНИЯ
# =========================================================================

# 1. Загружаем переменные из .env файла (например, DATABASE_URL)
load_dotenv()

# =========================================================================
# << КОНЕЦ ИСПРАВЛЕНИЯ
# =========================================================================


config = context.config

# =========================================================================
# >> НАЧАЛО ИСПРАВЛЕНИЯ
# =========================================================================

# 2. Определяем функцию get_database_url() ДО того, как она понадобится
#    (Этот код просто перенесен выше)
def get_database_url() -> str:
    return get_settings().database_url

# 3. Устанавливаем sqlalchemy.url в конфигурации Alembic
#    Это решает ошибку InterpolationMissingOptionError, так как
#    переменная %(DATABASE_URL)s в alembic.ini теперь будет проигнорирована
#    в пользу этого значения.
database_url = get_database_url()
if database_url:
    config.set_main_option("sqlalchemy.url", database_url)
else:
    print("ВНИМАНИЕ: DATABASE_URL не найдена. Проверьте .env файл.")

# =========================================================================
# << КОНЕЦ ИСПРАВЛЕНИЯ
# =========================================================================


if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


# (Эта функция была перенесена выше, до того как она понадобилась)
# def get_database_url() -> str:
#     return get_settings().database_url


def run_migrations_offline() -> None:
    context.configure(
        url=get_database_url(), # Используем уже установленный URL
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    # Теперь эта строка не вызовет ошибку, так как URL уже установлен
    configuration = config.get_section(config.config_ini_section) or {}
    
    # Эта строка больше не нужна, так как мы установили URL через set_main_option
    # configuration["sqlalchemy.url"] = get_database_url() 

    connectable = engine_from_config(
        configuration, # Использует 'sqlalchemy.url' который мы установили выше
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata, compare_type=True)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()