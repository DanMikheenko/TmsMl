def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

data = [-12, 1, 45, 2, 8, 0]

# display the sorted array
print(bubble_sort(data))
