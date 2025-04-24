import random

def quick_select(arr, k):
    if not arr:
        return None

    pivot = random.choice(arr)  # Випадковий pivot

    # Поділ елементів відносно опорного
    lows = [x for x in arr if x < pivot]      # Менші за pivot
    highs = [x for x in arr if x > pivot]     # Більші за pivot
    pivots = [x for x in arr if x == pivot]   # Рівні pivot

    if k <= len(lows):
        return quick_select(lows, k)  # k-й елемент серед менших
    elif k <= len(lows) + len(pivots):
        return pivot  # k-й елемент серед опорних
    else:
        # k-й елемент серед більших
        return quick_select(highs, k - len(lows) - len(pivots))
    

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(f"{k}-й найменший елемент: {quick_select(arr, k)}")

#       Quick Select	
# Рівні рекурсії (ділення)      log n (у середньому)	
# Робота на рівні               частина O(n)	
# Складність                    O(n) (серед.)