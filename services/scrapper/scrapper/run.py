import asyncio
from contextlib import closing
from provider import StsProvider


def run_scrapper():
    with closing(asyncio.get_event_loop()) as loop:

        StsProvider().get_menu()

        try:
            loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            loop.close()


if __name__ == "__main__":
    run_scrapper()
