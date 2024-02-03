import time
from typing import Tuple, List, Any

"""
Модуль быстрая сортировка
"""


def partition(list_input: list, first: int, last: int):
    """
    Функция для разделения массива в быстрой сортировки
    :param list_input:
    :param first:
    :param last:
    :return:
    """
    center = first
    for i in range(first + 1, last + 1):
        if list_input[i] <= list_input[first]:
            center += 1
            list_input[i], list_input[center] = list_input[center], list_input[i]
    list_input[center], list_input[first] = list_input[first], list_input[center]
    return center


def quick_sort(list_input, first=0, last=None):
    """
    На входе список не отсортированного массива.
    Функция сортирует алгоритмом подсчетом (быстрая сортировка) массив и отдает список вложенный в кортеж. Для решения
    задачи в этом нет необходимости, но возможность такая есть в случае доработки.
    Так-же функция замеряет время до начала сортировки и после, и отдает вторым элементом кортежа разницу.
    Так замеряется время выполнения сортировки в секундах.
    :param list_input: 
    :param first:
    :param last:
    :return: Tuple[list[int], float]
    """
    start_time = time.perf_counter()

    if last is None:
        last = len(list_input) - 1

    def internal_quick_sort(list_input: list, first: int, last: int):
        """
        Внутрення сортировка
        :param list_input:
        :param first:
        :param last:
        :return: list
        """
        if first >= last:
            return
        centr = partition(list_input, first, last)
        internal_quick_sort(list_input, first, centr - 1)
        internal_quick_sort(list_input, centr + 1, last)

    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return internal_quick_sort(list_input, first, last), execution_time
