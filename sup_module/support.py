"""
Модуль support для функций небольших сопровождающих и проверяющих функций
"""


def toFixed(number_float, quantity=0) -> str:
    """
    Функция обрезает значение float для наглядности.
    Принимает на вход значение float и значение количество знаков сколько необходимо обрезать
    :param quantity:
    :param number_float:
    :return:
    """
    return f"{number_float:.{quantity}f}"


def check_int_value(list_input: list) -> bool:
    """
    Функция целочисленной проверки списка.
    Возвращает True если проверка прошла успешно, False если не успешно или если список пустой.
    :param list_input:
    :return: Bool
    """
    res = True
    if len(list_input) == 0:
        res = False
    for i in list_input:
        if isinstance(i, int):
            continue
        else:
            res = False
            break
    return res


def test_input_list(list_input: list):
    if check_int_value(list_input):
        return "Данные валидны"
    else:
        if not list_input:
            return "Данных нет, список пустой"
        for i in list_input:
            if isinstance(i, float):
                return "В данных присутствует float"
            elif isinstance(i, str):
                return "В данных присутствует string"
