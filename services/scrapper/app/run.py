import asyncio
import logging
from contextlib import closing
from optparse import OptionParser

from provider import BetRadarMenuScrapper

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_menu_scrapper():
    with closing(asyncio.get_event_loop()) as loop:
        logger.info(f"Parse menu STS ")
        BetRadarMenuScrapper().fetch_menu_soccer()
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            logger.info("Received exit request, exiting")
        finally:
            loop.close()


def run_matches_scrapper():
    with closing(asyncio.get_event_loop()) as loop:
        logger.info(f"Parse menu STS ")
        BetRadarMenuScrapper().fetch_menu_soccer()
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            logger.info("Received exit request, exiting")
        finally:
            loop.close()


def main():
    parser = OptionParser()
    parser.add_option("--menu", dest="menu", help="scraping menu", nargs=0, type="string")
    parser.add_option("--matches", dest="matches", help="scraping matches", nargs=0, type="string")

    (options, args) = parser.parse_args()
    menu = options.menu if hasattr(options, "menu") else None
    matches = options.matches if hasattr(options, "matches") else None

    if menu:
        run_menu_scrapper()
    elif matches:
        run_matches_scrapper()


if __name__ == "__main__":
    main()
