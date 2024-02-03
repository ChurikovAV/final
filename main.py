from sort_module.bubble_sort import bubble_sort
from sort_module.counting_sort import counting_sort
from sort_module.quick_sort import quick_sort
from sort_module.radix_sort import radix_sort
from sup_module.support import *
import sys
from tkinter import *
from tkinter import ttk

sys.setrecursionlimit(9000)  # Увеличение глубины рекурсии

"""
Основной модуль программы сортировка
"""
# Тесты
if __name__ == '__main__':
    assert test_input_list([]) == 'Данных нет, список пустой'
    assert test_input_list([224, 759, 384, 109, 369, 133, 345, 562, 677, 220, 'd']) == 'В данных присутствует string'
    assert test_input_list([0.2, 224, 759, 384, 109, 369, 133, 345, 562, 677, 220]) == 'В данных присутствует float'
    assert test_input_list([224, 759, -384, -109, 369, 133, -345, 562, 677, 220]) == 'Данные валидны'


###################################################
def click_button() -> None:
    """
    Основная функция, в которой реализована логика работы интерфейса.
    В функции вызываются основные функции сортировки и связывая их с элементами дизайна.
    :return: None
    """
    label_error['text'] = ''
    label_result['text'] = ''
    if main_entry.get() == '':
        label_error['text'] = "Вы не ввели список чисел для сортировки!"
    else:
        list_input = main_entry.get().split(", ")
        list_output = []
        try:
            for x in list_input:
                list_output.append(int(x))
        except ValueError:
            label_error['text'] = 'Данные не корректные введите целые числа через запятую'
        list_output = [int(x) for x in list_input]
        if test_input_list(list_output) == 'Данные валидны':
            if combobox.get() == '':
                label_error['text'] = "Вы не выбрали сортировку"
            else:
                if combobox.get() == 'Bubble sort':
                    lis_sorted_bubble, bubble_time = bubble_sort(list_output)
                    label_result['text'] = f"{toFixed(bubble_time, 6)} сек"
                    main_entry.delete(0, END)
                    main_entry.insert(0, list_output)
                    print(main_entry.get().split(", "))
                elif combobox.get() == 'Counting sort':
                    lis_sorted_bubble, bubble_time = counting_sort(list_output)
                    label_result['text'] = f"{toFixed(bubble_time, 6)} сек"
                    main_entry.delete(0, END)
                    main_entry.insert(0, list_output)
                elif combobox.get() == 'Quick sort':
                    lis_sorted_bubble, bubble_time = quick_sort(list_output)
                    label_result['text'] = f"{toFixed(bubble_time, 6)} сек"
                    main_entry.delete(0, END)
                    main_entry.insert(0, list_output)
                elif combobox.get() == 'Radix sort':
                    lis_sorted_bubble, bubble_time = radix_sort(list_output)
                    label_result['text'] = f"{toFixed(bubble_time, 6)} сек"
                    main_entry.delete(0, END)
                    main_entry.insert(0, list_output)


root = Tk()
root.title("Алгоритмы - Итог: Анатолий Чуриков")
root.geometry("700x260+800+300")
root['bg'] = '#ced9e0'
root.resizable(False, False)

btn = ttk.Button(text="Расчет", width=20)
btn['command'] = click_button
btn.place(x=550, y=80, width=120, height=120)

label1 = ttk.Label(text="Выберите алгоритм: ", background='#ced9e0', font=("Arial", 12, "bold"))
label1.place(x=50, y=50, width=270, height=60)

sort_variables = ["Bubble sort", "Counting sort", "Quick sort", "Radix sort"]
combobox = ttk.Combobox(values=sort_variables)
combobox.place(x=30, y=100, width=190, height=25)

main_entry = ttk.Entry()
main_entry.place(x=30, y=30, width=640, height=30)

label_result = ttk.Label(text="!!!!!!!!!!!!",
                         font=("Arial", 14, "bold"),
                         foreground="#0f7520",
                         background='#ced9e0')
label_result.place(x=280, y=100, width=170, height=30)

label_error = ttk.Label(text="",
                        foreground="#f00",
                        background='#ced9e0',
                        font=("Arial", 12, "bold"))
label_error.place(x=30, y=150, width=490, height=40)

root.mainloop()
