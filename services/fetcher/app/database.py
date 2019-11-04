import logging
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


logger = logging.getLogger(__name__)


#dialect+driver://username:password@host:port/database


def setup() -> None:
    logger.info('initialize database connection')
    # create an engine
    # engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
    # 'mysql+pymysql:// :@localhost:3306/subscription_live
    engine = create_engine(f'mysql+pymysql://{os.env.MYSQL_ROOT_USER}:{os.env.MYSQL_ROOT_PASSWORD}@localhost:3306/{os.env.MYSQL_DATABASE}')


    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()
    return session


session = setup()
