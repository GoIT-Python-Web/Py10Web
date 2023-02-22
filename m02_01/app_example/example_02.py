import logging
from logger import get_logger

logger = get_logger(__name__)


def foo(num: int):
    result = num + 100
    logger.info(result)
    logger.debug(f"num: {num}, result: {result}")

    return result


def baz():
    logger.error("Error!")


if __name__ == "__main__":
    logger.log(level=logging.DEBUG, msg=f"Start")
    foo(10)
    baz()
