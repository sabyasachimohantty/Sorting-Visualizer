insertionsort_animate = []

def insertionsort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1
        while j >= 0 and val < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            insertionsort_animate.append(arr.copy())
        
        arr[j + 1] = val
        insertionsort_animate.append(arr.copy())        
