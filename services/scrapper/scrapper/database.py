import logging
import os

import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

logger = logging.getLogger(__name__)


# dialect+driver://username:password@host:port/database


def setup():
    logger.info("initialize database connection")
    # create an engine
    # engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
    # 'mysql+pymysql:// :@localhost:3306/subscription_live

    engine = create_engine(
        f"mysql+pymysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_HOST or 'mysql'}:3306/{config.MYSQL_DATABASE}"
    )
    # engine = create_engine(f"mysql+pymysql://{settings.get('MYSQL_ROOT_USER', 'root')}:{settings.get('MYSQL_ROOT_PASSWORD', 'root')}@{settings.get('MYSQL_ROOT_HOST', '172.23.0.2')}:3306/{settings.get('MYSQL_DATABASE', 'stsparser')}")
    # engine = create_engine(f"mysql+pymysql://{settings.get('MYSQL_ROOT_USER', 'root')}:{settings.get('MYSQL_ROOT_PASSWORD', 'root')}@172.23.0.2:3306/{settings.get('MYSQL_DATABASE', 'stsparser')}")

    # create a configured "Session" class
    Session = sessionmaker(bind=engine, autoflush=True)

    # create a Session
    session = Session()
    return session


session = setup()
