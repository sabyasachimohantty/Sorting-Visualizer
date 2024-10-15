mergesort_animate = []

def merge(arr, l, m, r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    i = l
    j, k = 0, 0
    while j < len(left) and k < len(right):
        if left[j] <= right[k]:
            arr[i] = left[j]
            j += 1
        else:
            arr[i] = right[k]
            k += 1
        i += 1
        mergesort_animate.append(arr.copy())
        
    while j < len(left):
        arr[i] = left[j]
        j += 1
        i += 1
        mergesort_animate.append(arr.copy())
    
    while k < len(right):
        arr[i] = right[k]
        k += 1
        i += 1
        mergesort_animate.append(arr.copy())

    mergesort_animate.append(arr.copy())

def mergesort(arr, l, r):
    if l == r:
        return
    m = (l + r) // 2
    mergesort(arr, l, m)
    mergesort(arr, m + 1, r)
    merge(arr, l, m, r)
