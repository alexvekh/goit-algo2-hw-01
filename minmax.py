def find_min_max(arr):
    # один елемент
    if len(arr) == 1:
        return (arr[0], arr[0])
    
    # два елементи
    if len(arr) == 2:
        return (min(arr[0], arr[1]), max(arr[0], arr[1]))
    
    # решта випадків - рекурсивно ділимо елеиенти
    mid = len(arr) // 2
    left_min_max = find_min_max(arr[:mid])
    right_min_max = find_min_max(arr[mid:])
    
    # Об'єднуємо результати
    overall_min = min(left_min_max[0], right_min_max[0])
    overall_max = max(left_min_max[1], right_min_max[1])
    
    return (overall_min, overall_max)

arr = [7, 2, 9, 4, 1, 5]
print(find_min_max(arr))  # Виведе: (1, 9)

#  Глибина рекурсії	        log n
#  Робота на кожному рівні	O(1)
#  Загальна складність      O(n)