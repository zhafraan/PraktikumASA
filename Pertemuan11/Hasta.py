# Input jumlah materi dan total waktu
N, T = map(int, input().split())

# Membuat tabel DP
materi = [0] * (T + 1)

# Membaca setiap materi
for i in range(N):

    waktu, kepentingan, kesulitan, latihan = map(int, input().split())

    # Menghitung nilai manfaat
    nilai = (kepentingan * 10) + (latihan * 5) - (kesulitan * 2)

    # Bottom-Up Dynamic Programming
    # Dari belakang agar setiap materi hanya dipilih 1 kali
    for t in range(T, waktu - 1, -1):

        materi[t] = max(materi[t], materi[t - waktu] + nilai)

# Output nilai maksimum
print(materi[T])