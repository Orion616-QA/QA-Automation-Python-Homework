import logging

"""Генератори-------"""
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

"""Ітератори-------"""

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 2
        return value

"""Декоратори-------"""

def log_args_and_result(func):

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logger = logging.getLogger(func.__module__)

    def data_and_result(*args, **kwargs):
        text_args = []
        for a in args:
            text_args.append(str(a))
        for k, v in kwargs.items():
            text_args.append(f"{k}={v}")
        args_str = ", ".join(text_args)

        logger.info(f"Data: {func.__name__}({args_str})")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Result: {func.__name__} -> {result}")
            return result
        except Exception as e:
            logger.error(f"Exception in {func.__name__}: {e}")
            raise

    return data_and_result

def handle_exceptions(func):
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logger = logging.getLogger(func.__module__)

    def data(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Exception in {func.__name__}: {e}")
            return f"Exception: {e}"

    return data