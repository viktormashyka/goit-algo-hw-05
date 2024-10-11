# Реалізуйте двійковий пошук для відсортованого масиву з дробовими числами. Написана функція 
# для двійкового пошуку повинна повертати кортеж, де першим елементом є кількість ітерацій, 
# потрібних для знаходження елемента. Другим елементом має бути "верхня межа" — це найменший елемент, 
# який є більшим або рівним заданому значенню.

# Виконання коду повертає кортеж, де першим елементом є кількість ітерацій, потрібних 
# для знаходження елемента. Другим елементом є "верхня межа" (найменший елемент, який є більшим 
# або рівним заданому значенню).

def binary_search(arr, target):
    """
    Функція для бінарного пошуку елемента в відсортованому масиві.

    Parameters:
    arr (list): Відсортований масив для пошуку.
    target: Елемент, який шукаємо.

    Returns:
    int: Індекс елемента в масиві або -1, якщо елемент не знайдено.
    """
    left = 0  # Ліва межа масиву
    right = len(arr) - 1  # Права межа масиву
    count = 0 # Лічильник ітерацій
    upper_bound = None # Верхня межа

    while left <= right:
        count += 1
        mid = (left + right) // 2  # Знаходимо середину масиву

        if arr[mid] == target:
            return count, arr[mid]  # Якщо знайдено шуканий елемент, повертаємо кількість ітерацій та сам елемент
        elif arr[mid] < target:
            left = mid + 1  # Якщо шуканий елемент більший, зміщуємо ліву межу
        else:
            upper_bound = arr[mid]  # Запам'ятовуємо "верхню межу"
            right = mid - 1  # Якщо шуканий елемент менший, зміщуємо праву межу


    return count, upper_bound # Повертаємо кількість ітерацій та "верхню межу"

# Приклад використання
array = [86/91, 12/38, 3/8, 8/12, 3/16, 18/23, 1/2, 3/5, 15/56, 54/72]
target = 3/5
sorted_array = sorted(array)
count, upper_bound = binary_search(sorted_array, target)

print(f"Кількість ітерацій: {count}\t Верхня межа: {upper_bound}")