def UrutinDatanya(data):
    # pake insertion sort buat ngurutin datanya karena ga tau buat ngurutinnya sebenernya gimana yang lebih mudah belum kepikiran yang kepirian cuman pake insertion
    for i in range(1, len(data)):
        kunci = data[i]
        j = i - 1
        while j >= 0 and data[j] > kunci:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = kunci
    return data

def CariSarang(Sarang, energitoday):
    # binary search buat cari sarang yang bisa di panen
    kiri = 0
    kanan = len(Sarang) - 1
    hasil = -1
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if Sarang[tengah] <= energitoday:
            hasil = tengah
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return hasil

# inputannya
jmlsarang, jmlhari = map(int, input().split())
Sarang = list(map(int, input().split()))
energitoday = list(map(int, input().split()))

# Urutkan tingkat sarang pake insertion sort sebelumnnya
Sarang = UrutinDatanya(Sarang)
totalndog = 0
for hariini in energitoday:
    idx_last = CariSarang(Sarang, hariini)
    
    if idx_last >= 0:
        totalndog += idx_last + 1

print(totalndog)