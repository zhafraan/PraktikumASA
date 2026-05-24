n = int(input())
arr = list(map(int, input().split()))
# Mengurutkan berat dari terbesar ke terkecil
arr.sort(reverse=True)
# hasil terbaik, -1 jika tidak ada kombinasi valid
hasil = -1
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            Wa = arr[i]
            Wb = arr[j]
            Wc = arr[k]
            # Hitung nilai S
            S = (Wa * Wb) + (Wb * Wc) + (Wc * Wa)
            # Cek syarat ganjil S
            if S % 2 == 1:
                # Ambil total berat terbesar yang valid
                total = Wa + Wb + Wc
                if total > hasil:
                    hasil = total

print(hasil)