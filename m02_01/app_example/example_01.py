import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(funcName)15s %(lineno)d - %(message)s"
)


def foo(num: int):
    result = num + 100
    logging.info(result)
    logging.debug(f"num: {num}, result: {result}")
    return result


if __name__ == "__main__":
    foo(10)
