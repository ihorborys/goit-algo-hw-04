import random
import timeit

# """Генеруємо список з 20 випадкових чисел"""
# data_list = [random.randint(1, 100) for _ in range(20)]
# print(f"Згенерований список 20 випадкових чисел: {data_list}")

"""Генеруємо список з 100 випадкових чисел"""
data_list = [random.randint(1, 1000) for _ in range(100)]
print(f"Згенерований список 100 випадкових чисел: {data_list}")


"""Обчислюємо час сортування функцією' sort (гібридний алгоритм Timesort)"""
time_sorted = timeit.timeit('sorted(data_list)', globals=globals(), number=1000)
print(f"Час виконання алгоритмом sorted: {time_sorted} секунд")

"""Обчислюємо час сортування функцією sorted (гібридний алгоритм Timesort)"""
time_sort = timeit.timeit('data_list.sort()', globals=globals(), number=1000)
print(f"Час виконання алгоритмом sort: {time_sort} секунд")


"""Обчислюємо час сортування алгоритмом вставки ітеративним методом"""
def insertion_sort(lst):
    for i in range(1, len(lst)):  # Починаємо з другого елемента масиву
        key = lst[i]  # Зберігаємо поточний елемент як ключ
        j = i - 1  # Починаємо порівнювати з попереднім елементом
        while j >= 0 and key < lst[j]:  # Поки не дійшли до початку масиву і ключ менший за поточний елемент
            lst[j + 1] = lst[j]  # Зсуваємо поточний елемент вправо
            j -= 1  # Переміщаємось на одну позицію вліво
        lst[j + 1] = key  # Вставляємо ключ на правильну позицію
    return lst  # Повертаємо відсортований масив

time_insert_iterative = timeit.timeit('insertion_sort(data_list)', globals=globals(), number=1000)
print(f"Час виконання алгоритмом вставки (ітеративно): {time_insert_iterative} секунд")

"""Обчислюємо час сортування алгоритмом вставки рекурсивним методом"""
def insertion_sort_recursive(arr, n):
    if n <= 1:  # Базовий випадок: якщо масив має один або менше елементів, він вже відсортований
        return

    insertion_sort_recursive(arr, n - 1)  # Сортуємо перші n-1 елементів рекурсивно

    key = arr[n - 1]  # Зберігаємо останній елемент як ключ
    j = n - 2  # Починаємо порівнювати з попереднім елементом
    while j >= 0 and arr[j] > key:  # Поки не дійшли до початку масиву і ключ менший за поточний елемент
        arr[j + 1] = arr[j]  # Зсуваємо поточний елемент вправо
        j -= 1  # Переміщаємось на одну позицію вліво
    arr[j + 1] = key  # Вставляємо ключ на правильну позицію
    return arr  # Повертаємо відсортований масив

time_insert_recursive = timeit.timeit('insertion_sort_recursive(data_list, len(data_list))', globals=globals(), number=1000)
print(f"Час виконання алгоритмом вставки (рекурсивно): {time_insert_recursive} секунд")


# Функція злиття підмасивів
def merge(array, left, middle, right):
    n1 = middle - left + 1  # Довжина першого підмасиву
    n2 = right - middle  # Довжина другого підмасиву

    left_array = [0] * n1  # Тимчасовий масив для першого підмасиву
    right_array = [0] * n2  # Тимчасовий масив для другого підмасиву

    # Копіюємо дані в тимчасові масиви
    for i in range(0, n1):
        left_array[i] = array[left + i]
    for i in range(0, n2):
        right_array[i] = array[middle + i + 1]

    i, j, k = 0, 0, left
    # Злиття двох тимчасових масивів у основний масив
    while i < n1 and j < n2:
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    # Додавання залишкових елементів з першого та другого підмасивів
    while i < n1:
        array[k] = left_array[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = right_array[j]
        j += 1
        k += 1

"""Обчислюємо час сортування злиттям знизу вгору (ітеративно)"""
def merge_sort_bottom_up(array):
    width = 1  # Починаємо з мінімального розміру підмасиву, 2^0 = 1
    length = len(array)
    while width < length:  # Поки розмір підмасиву менший за загальну довжину масиву
        left = 0
        while left < length:  # Проходимо по масиву зліва направо
            right = min(left + (width * 2 - 1), length - 1)  # Визначаємо праву межу для об'єднання
            middle = min(left + width - 1, length - 1)  # Визначаємо середню межу для об'єднання
            merge(array, left, middle, right)  # Злиття двох підмасивів
            left += width * 2  # Переходимо до наступного підмасиву
        width *= 2  # Збільшуємо розмір підмасиву вдвічі на кожній ітерації
    return array  # Повертаємо відсортований масив
time_merge_iterative = timeit.timeit('merge_sort_bottom_up(data_list)', globals=globals(), number=1000)
print(f"Час виконання алгоритмом злиття (ітеративно): {time_merge_iterative} секунд")


# Функція злиття двох відсортованих масивів
def merge(left, right):
    result = []  # Результуючий масив
    left_index, right_index = 0, 0  # Індекси для лівого і правого масивів

    # Зливаємо масиви, порівнюючи елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Додаємо залишкові елементи з обох масивів
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result  # Повертаємо злитий масив

"""Обчислюємо час сортування злиттям рекурсивно"""
def merge_sort_recursive(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort_recursive(left_half)
    right_half = merge_sort_recursive(right_half)

    return merge(left_half, right_half)  # Виклик функції злиття для двох підмасивів

time_merge_recursive = timeit.timeit('merge_sort_recursive(data_list)', globals=globals(), number=1000)
print(f"Час виконання алгоритмом злиття (рекурсивно): {time_merge_recursive} секунд")