n = int(input())
arr = list(map(int, input().split()))
# Input matriks tambahan
matriks = []
for i in range(n):
    baris = list(map(int, input().split()))
    matriks.append(baris)
best = [-1]  # hasil minimum 

def coba(urutan, sisa):
    if len(sisa) == 0:
        # Hitung total kelelahan untuk urutan ini
        total = 0
        for step in range(n):
            after = urutan[step]
            total += arr[after]
            if step > 0:
                before = urutan[step - 1]
                total += matriks[after][before]
        # Simpan total terkecil
        if best[0] == -1 or total < best[0]:
            best[0] = total
        return

    for x in sisa:
        sisabaru = [y for y in sisa if y != x]
        coba(urutan + [x], sisabaru)
coba([], list(range(n)))
print(best[0])