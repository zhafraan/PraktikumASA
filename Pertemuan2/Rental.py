N, M, X = map(int, input().split())
P = [0] * N
V = [0] * N
C = [0] * N
for i in range(N):
    P[i], V[i], C[i] = map(int, input().split())

def solve(i, total_p, total_v, total_c):
    if i == N:
        if total_p >= M and total_v >= X:
            return total_c
        else:
            return 10**18
    ambil = solve(i + 1,total_p + P[i],total_v + V[i],total_c + C[i])
    
    tidak_ambil = solve(i + 1,total_p,total_v,total_c)
    if ambil < tidak_ambil:
        return ambil
    else:
        return tidak_ambil

hasil = solve(0, 0, 0, 0)
if hasil == 10**18:
    print(-1)
else:
    print(hasil)