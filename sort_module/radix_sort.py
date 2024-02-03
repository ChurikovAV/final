import time
from typing import Union, List, Any, Tuple

"""
Модуль поразрядная сортировка
"""


def radix_sort(list_input: list) -> tuple[list[int], float]:
    """

    :param list_input:
    :return: Tuple[list[int], float]
    """
    start_time = time.perf_counter()
    max_digits = max([len(str(x)) for x in list_input])
    base = 10
    bins = [[] for _ in range(base)]

    for i in range(0, max_digits):
        for x in list_input:
            digit = (x // base ** i) % base
            bins[digit].append(x)
        list_input = [x for queue in bins for x in queue]

        bins = [[] for _ in range(base)]
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return list_input, execution_time
