# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# engine = create_engine('sqlite:///:memory:', echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()

import typing
import logging
import os
from aiohttp import web
from asyncpg import pool
from dynaconf import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = web.Application()


def setup(app: web.Application) -> None:
    app.cleanup_ctx.append(db_setup)


async def db_setup(app: web.Application) -> typing.AsyncIterator[None]:
    logger.info('Initialize db connection')
    app['db_pool'] = await pool.create_pool(
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        database=settings.DB_NAME,
        host=settings.DB_HOST,
        port=5432
    )
    yield
    logger.info('Closing db connection')
    await db_pool.close()


if __name__ == '__main__':
    logger.info('Initializing siteparser')
    setup(app)
