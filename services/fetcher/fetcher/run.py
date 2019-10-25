# from fetcher.tasks import fetch_url
# if __name__ == '__main__':
#     url = ['http://example1.com' , 'http://example2.com' , 'http://example3.com' , 'http://example4.com' , 'http://example5.com' , 'http://example6.com' , 'http://example7.com' , 'http://example8.com'] # change them to your ur list.
#     for i in url:
#         result = longtime_add.delay(i)
#         print 'Task result:',result.result


from provider import BetRadarProvider
import asyncio
import logging
from contextlib import closing


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
