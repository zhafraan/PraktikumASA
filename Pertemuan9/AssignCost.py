#input
N = int(input())
pekerja = list(range(N))
cost = []
for _ in range(N):
    baris = list(map(int, input().split()))
    cost = cost + [baris]

#hitung perkiraan batas bawah biaya dari penugasan saat ini
def hitungbound(idx_pekerja, tugas, cost_saat_ini):
    bound = cost_saat_ini
    for i in range(idx_pekerja, N):
        minimum = float('inf')
        for j in range(N):
            if not tugas[j]:
                if cost[i][j] < minimum:
                    minimum = cost[i][j]
        bound += minimum
    return bound

#branch and Bound buat assign tugas ke pekerja dengan biaya minimum
def assignBNB():
    best_cost = [float('inf')]
    tugas = [False] * N
    #dfs buat menjelajahi semua kemungkinan tugas yang diberikan
    def dfs(idx_pekerja, tugas, cost_saat_ini):
        # jika semua pekerjanya sudah ditugaskan, 
        # lihat biaya saat ini apa lebih baik dibandingkan dengan biaya terbaik yang ditemukan 
        if idx_pekerja == N: #jia semua pekerja sudah ditugaskan
            if cost_saat_ini < best_cost[0]:
                best_cost[0] = cost_saat_ini
            return
        #coba untuk setiap tugas yang belum ditugaskan 
        for j in range(N):
            if not tugas[j]:
                cost_baru = cost_saat_ini + cost[idx_pekerja][j]
                bound = hitungbound(idx_pekerja + 1, tugas, cost_baru)
                if bound < best_cost[0]:
                    tugas[j] = True
                    dfs(idx_pekerja + 1, tugas, cost_baru)
                    tugas[j] = False  #backtrack untuk mencoba tugas selanjutnya
                    
    #mulai dfs dari pekerja pertama 
    dfs(0, tugas, 0)
    return best_cost[0]

#jalankan output
print(assignBNB())