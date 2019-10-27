from provider import BetRadarProvider
import asyncio
import logging
from contextlib import closing
import requests


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_fetcher():
    with closing(asyncio.get_event_loop()) as loop:
        logger.info(f"Parse menu STS ")
        BetRadarProvider().fetch_menu()
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            logger.info("Received exit request, exiting")
        finally:
            loop.close()


if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings()
    run_fetcher()
