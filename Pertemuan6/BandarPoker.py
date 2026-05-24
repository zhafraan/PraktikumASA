# Fungsi quicksort
def quickSort(arr, low, high):
    global iterator
    iterator += 1  # menghitung setiap pemanggilan quicksort

    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Fungsi partition (pivot = elemen paling kanan)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1

            # swap
            arr[i], arr[j] = arr[j], arr[i]

    # pindahkan pivot ke posisi benar
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# Input
N = int(input())
A = list(map(int, input().split()))
maxIter = -1
minIter = 10**9
worstPivot = A[0]
bestPivot = A[0]

# Coba setiap elemen jadi pivot awal
for i in range(N):

    # copy array asli
    tempArr = A.copy()

    # swap elemen i dengan elemen terakhir
    tempArr[i], tempArr[N - 1] = tempArr[N - 1], tempArr[i]

    # reset iterator
    iterator = 0

    # jalankan quicksort
    quickSort(tempArr, 0, N - 1)

    # cek iterasi maksimal
    if iterator > maxIter:
        maxIter = iterator
        worstPivot = A[i]

    # cek iterasi minimal
    if iterator < minIter:
        minIter = iterator
        bestPivot = A[i]

# Output
print(worstPivot)
print(bestPivot)