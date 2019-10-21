import asyncio
import logging
from aiohttp import web
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import closing
import database

logger = logging.getLogger(__name__)

logger.info('Initializing Application')

app = web.Application()


# engine = create_engine('sqlite:///:memory:', echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()


def run_fetcher():
    with closing(asyncio.get_event_loop()) as loop:

        logger.info(f"Receiver Started")
        Fetcher().receive_messages()

        try:
            loop.run_forever()
        except KeyboardInterrupt:
            logger.info("Received exit request, exiting")
        finally:
            loop.close()


if __name__ == '__main__':
    database.setup(app)
