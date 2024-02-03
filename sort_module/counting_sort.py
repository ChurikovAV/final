import time

"""
Модуль сортировка подсчетом
"""


def counting_sort(list_input: list) -> tuple[list[int], float]:
    """
    На входе список не отсортированного массива. Функция сортирует алгоритмом подсчета массив и отдает список
    вложенный в кортеж. Для решения задачи в этом нет необходимости, но возможность такая есть в случае доработки.
    Так-же функция замеряет время до начала сортировки и после, и отдает вторым элементом кортежа разницу. Так
    замеряется время выполнения сортировки в секундах.
    :param list_input:
    :return: Tuple[list[int], float]
    """
    start_time = time.perf_counter()
    max_element = max(list_input)
    list_output = [0] * len(list_input)
    low = min(list_input)
    high = max(list_input)
    count_array = [0 for i in range(low, high + 1)]
    for i in list_input:
        count_array[i - low] += 1
    for j in range(1, len(count_array)):
        count_array[j] += count_array[j - 1]
    for k in reversed(list_input):
        list_output[count_array[k - low] - 1] = k
        count_array[k - low] -= 1

    end_time = time.perf_counter()
    execution_time = end_time - start_time

    return list_output, execution_time
