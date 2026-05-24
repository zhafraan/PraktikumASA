# ini buat algoritma partisi untuk bagi array sesuai pivot nya
def partition(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1

#ini algoritma quick short nya
def quicksort(a, low, high):
    if low < high:
        pi = partition(a, low, high)
        quicksort(a, low, pi - 1)
        quicksort(a, pi + 1, high)
        
#inputannya
n = int(input())
a = list(map(int, input().split()))
quicksort(a, 0, n - 1)
print(*a)