N, T = 3, 15
d = [5, 4, 7]
f = [5, 6, 3]

def backtrack(sisa_waktu, last_idx, fokus):
    if sisa_waktu <= 0:
        return fokus
    best = fokus
    for i in range(N):
        if d[i] < 5 and i != last_idx and d[i] <= sisa_waktu:
            hasil = backtrack(sisa_waktu - d[i], i, fokus + f[i])
            if hasil > best:
                best = hasil
    return best

print(backtrack(T, -1, 0))