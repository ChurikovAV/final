import time
from typing import Tuple

"""
Модуль сортировка пузырьком
"""


def bubble_sort(list_input: list) -> tuple[list[int], float]:
    """
    На входе список не отсортированного массива.
    Функция сортирует алгоритмом пузырек массив и отдает список вложенный в кортеж. Для решения задачи в этом нет необходимости,
    но возможность такая есть в случае доработки.
    Так-же функция замеряет время до начала сортировки и после, и отдает вторым элементом кортежа разницу.
    Так замеряется время выполнения сортировки в секундах.
    :param list_input:
    :return: Tuple[list[int], float]
    """
    start_time = time.perf_counter()

    for i in range(0, len(list_input) - 1):
        for j in range(len(list_input) - 1):
            if list_input[j] > list_input[j + 1]:
                temp = list_input[j]
                list_input[j] = list_input[j + 1]
                list_input[j + 1] = temp

    end_time = time.perf_counter()
    execution_time = end_time - start_time

    return list_input, execution_time
