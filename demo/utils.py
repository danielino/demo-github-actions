import datetime
from typing import Any


def somma(a, b) -> Any[int, float]:
    """
    function that return sum of args
    :param a:
    :param b:
    :return: int|float
    """
    return a + b

def moltiplicazione(a, b) -> Any[int, float]:
    """
    function that return multiplication of args
    :param a:
    :param b:
    :return:
    """
    return a * b


def get_date_iso_now() -> str:
    """
    return current date time in iso format
    :return: str
    """
    return datetime.datetime.now().isoformat()

