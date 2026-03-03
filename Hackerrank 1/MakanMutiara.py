# Input nilai awal
Awal = list(map(int, input().split()))
N = Awal[0]
Y = Awal[1] + 1
X = Awal[2]

# Input kondisi jalan
lintasan = list(map(int, input().split()))
mutiara = 0          # jumlah mutiara yang terkumpul
pos = 0           
masihJalan = True   

while pos < N and masihJalan:
    isi = lintasan[pos]
    # Ambil efek dari isi jalan
    if isi < 7:
        Y += isi
    elif isi == 7:
        mutiara += 1
    # Cek tenaga sebelum jalan
    if Y == 0:
        if mutiara > 0:
            mutiara -= 1
            Y += 7
        else:
            masihJalan = False
    # Kalau masih bisa jalan, lanjut
    if masihJalan:
        Y -= 1
        pos += 1
# Cek hasil akhir
if pos == N and mutiara >= X:
    print(mutiara)
else:
    print(-1)