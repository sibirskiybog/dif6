"""
Модуль list_operations.py содержит функции для работы со списками:
- фильтрация элементов по предикату
- преобразование элементов списка
- группировка элементов по ключу
"""


def filter_list(input_list, predicate):
    """
    Фильтрует список по заданному предикату.

    Аргументы:
        input_list (list): Исходный список целых чисел
        predicate (function): Функция-предикат, возвращающая bool для каждого элемента

    Возвращает:
        list: Новый список, содержащий только элементы, для которых предикат вернул True
    """
    # Используем list comprehension для фильтрации с применением предиката
    return [element for element in input_list if predicate(element)]


def transform_list(input_list, transform_func):
    """
    Преобразует элементы списка с помощью заданной функции.

    Аргументы:
        input_list (list): Исходный список строк
        transform_func (function): Функция преобразования строк

    Возвращает:
        list: Новый список с преобразованными элементами
    """
    # Применяем функцию преобразования к каждому элементу списка
    return [transform_func(element) for element in input_list]


def group_by_key(object_list, key_selector):
    """
    Группирует объекты списка по заданному ключу.

    Аргументы:
        object_list (list): Список объектов для группировки
        key_selector (function): Функция, возвращающая ключ для каждого объекта

    Возвращает:
        dict: Словарь с группированными объектами, где ключи - значения key_selector
    """
    grouped_dict = {}

    for obj in object_list:
        # Получаем ключ для текущего объекта
        key = key_selector(obj)

        # Если ключа еще нет в словаре, создаем пустой список
        if key not in grouped_dict:
            grouped_dict[key] = []

        # Добавляем объект в соответствующую группу
        grouped_dict[key].append(obj)

    return grouped_dict


# Примеры использования функций
if __name__ == "__main__":
    # Пример фильтрации: оставить только четные числа
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = filter_list(numbers, lambda x: x % 2 == 0)
    print("Четные числа:", even_numbers)

    # Пример преобразования: преобразовать строки в их длины
    strings = ["яблоко", "банан", "черешня"]
    lengths = transform_list(strings, len)
    print("Длины строк:", lengths)

    # Пример группировки: сгруппировать слова по первой букве
    words = ["яблоко", "банан", "черешня", "арбуз", "ананас"]
    grouped_words = group_by_key(words, lambda x: x[0])
    print("Слова по первой букве:", grouped_words)
