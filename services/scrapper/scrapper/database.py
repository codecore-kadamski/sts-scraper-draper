import logging
import os
import typing

from aiohttp import web
#  from asyncpg import pool
import aiomysql

logger = logging.getLogger(__name__)


def setup(app: web.Application, dbtype) -> None:
    app.cleanup_ctx.append(db_setup)


async def db_setup(app: web.Application) -> typing.AsyncIterator[None]:
    logger.info('initialize database connection')

    # if dbtype == 'pq':
    #     app['db_pool'] = db_pool = await pool.create_pool(
    #         user=os.getenv('POSTGRES_USER'),
    #         password=os.getenv('POSTGRES_PASSWORD'),
    #         database=os.getenv('POSTGRES_DB'),
    #         host=os.getenv('POSTGRES_HOST', '127.0.0.1'),
    #         port=os.getenv('POSTGRES_PORT', 5432),
    #     )
    app['db_pool'] = db_pool = await aiomysql.create_pool.create_pool(
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE'),
        host=os.getenv('MYSQL_HOST', '127.0.0.1'),
        port=os.getenv('MYSQL_PORT', 3306),
    )
    yield
    logger.info('Closing database connection')
    await db_pool.close()
