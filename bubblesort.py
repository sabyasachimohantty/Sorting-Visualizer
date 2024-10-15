bubblesort_animate = []

def bubblesort(arr):
    for i in reversed(range(len(arr))):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            bubblesort_animate.append(arr.copy())
