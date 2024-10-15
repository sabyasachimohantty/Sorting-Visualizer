quicksort_animate = []

def quicksort(arr, i, j):
    if j <= i:
        return
    p = partition(arr, j, i, j - 1)
    quicksort(arr, i, p - 1)
    quicksort(arr, p + 1, j)

def partition(arr, p, i, j):
    while i < j:
        while i < p and arr[i] <= arr[p]:
            i += 1
        while j > i and arr[j] > arr[p]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            quicksort_animate.append(arr.copy())

    if arr[i] > arr[p]:
        arr[i], arr[p] = arr[p], arr[i]
        quicksort_animate.append(arr.copy())

    return i
