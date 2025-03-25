def maxmin_select(arr, left, right):
    if left == right:
        return arr[left], arr[left]  # Caso base: um único elemento
    
    if right - left == 1:
        return (arr[left], arr[right]) if arr[left] < arr[right] else (arr[right], arr[left])
    
    mid = (left + right) // 2
    min1, max1 = maxmin_select(arr, left, mid)
    min2, max2 = maxmin_select(arr, mid + 1, right)
    
    return min(min1, min2), max(max1, max2)

def main():
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    min_val, max_val = maxmin_select(arr, 0, len(arr) - 1)
    print(f"Menor elemento: {min_val}")
    print(f"Maior elemento: {max_val}")

if __name__ == "__main__":
    main()