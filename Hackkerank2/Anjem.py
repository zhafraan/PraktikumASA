n = int(input())
jarak = [[0] * n for i in range(n)]
for i in range(n):
    baris = list(map(int, input().split()))
    for j in range(n):
        jarak[i][j] = baris[j]
    Daerah = ['A', 'B', 'C', 'D', 'E']

def search(posisi, sudah_dikunjungi, jalur, total):
    if len(jalur) == n:
        return total + jarak[posisi][0], jalur + [0]

    shortes = (999999999, [])
    for i in range(1, n):
        if not sudah_dikunjungi[i]:
            sudah_dikunjungi[i] = True
            hasil = search(i, sudah_dikunjungi, jalur + [i], total + jarak[posisi][i])
            if hasil[0] < shortes[0]:
                shortes = hasil
            sudah_dikunjungi[i] = False
    return shortes

tandai = [False] * n
tandai[0] = True
jarak_min, Ruteoptimal = search(0, tandai, [0], 0)

print(jarak_min)
print(*[Daerah[i] for i in Ruteoptimal])