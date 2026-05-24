def LeleNakal(arr):
    # merge sort 
    if len(arr) <= 1:
        return arr, 0
    tengah= len(arr) // 2
    left, i_kiri= LeleNakal(arr[:tengah])
    right, i_kanan = LeleNakal(arr[tengah:])

    n = len(arr)
    merged = [0] * n
    i,j,k = 0,0,0
    # hitung inversi
    Inversi = i_kiri + i_kanan
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            Inversi += len(left) - i
            j += 1
        k += 1

    while i < len(left):
        merged[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        merged[k] = right[j]
        j += 1
        k += 1
    return merged, Inversi

n = int(input())
arr = list(map(int, input().split()))

_, Inversi = LeleNakal(arr)
print(Inversi)
