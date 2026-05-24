def MBG(arr, kiri, kanan):
    if kiri == kanan:# basis
        return arr[kiri], arr[kiri]
    elif kanan == kiri + 1:
        if arr[kiri] < arr[kanan]:
            return arr[kiri], arr[kanan]
        else:
            return arr[kanan], arr[kiri]
    # devide  
    tengah = (kiri + kanan) // 2
    # conquer
    min1, max1 = MBG(arr, kiri, tengah)
    min2, max2 = MBG(arr, tengah + 1, kanan)
    #combine
    if min1 < min2:
        minimum = min1
    else:
        minimum = min2
    if max1 > max2:
        maksimum = max1
    else:
        maksimum = max2
    return minimum, maksimum

n = int(input())
arr = list(map(int, input().split()))
minimum, maksimum = MBG(arr, 0, n - 1)
print(minimum, maksimum)  