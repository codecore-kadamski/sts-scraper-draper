import logging
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


logger = logging.getLogger(__name__)


def setup() -> None:
    logger.info('initialize database connection')
    # create an engine
    engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()
    return session


session = setup()
