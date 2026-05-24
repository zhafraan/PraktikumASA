# inputan
n = int(input())
kota = list(range(n))
jarak = []
for _ in range(n):
    baris = list(map(int, input().split()))
    jarak = jarak + [baris]
awal = 0  # indeks awal

# Hitung perkiraan batas bawah biaya
def hitungbound(visited, cost_sekarang):
    bound = cost_sekarang
    for i in range(len(kota)):
        if not visited[i]:
            minimum = float("inf")
            for j in range(len(kota)):
                if i != j and jarak[i][j] < minimum:
                    minimum = jarak[i][j]
            bound += minimum
    return bound

# Untuk Branch and Bound
def tspBNB():
    best_cost = [float("inf")]
    best_rute = [[]]
    visited = [False] * len(kota)
    visited[awal] = True
    ##Dfs untuk menjelajahi semua kemungkinan rute
    def dfs(posisi, visited, rute, biaya):
        if len(rute) == len(kota):
            total = biaya + jarak[posisi][awal]
            if total < best_cost[0]:
                best_cost[0] = total
                best_rute[0] = rute + [awal]
            return
        for i in range(len(kota)):
            if not visited[i]:
                cost_baru = biaya + jarak[posisi][i]
                bound = hitungbound(visited, cost_baru)
                if bound < best_cost[0]:
                    visited[i] = True
                    dfs(i, visited, rute + [i], cost_baru)
                    visited[i] = False  
    dfs(awal, visited, [awal], 0) #backtrack mulai dari kota awal
    return best_rute[0], best_cost[0]

# jalankan output
rute, total = tspBNB()
print(total)