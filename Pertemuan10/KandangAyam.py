# input
N, M = map(int, input().split())
# untuk menyimpan nilai heuristik dan graph
heuristik = {}
graph     = {}
for i in range(N):
    nama, h   = input().split()
    heuristik[nama] = int(h)
    graph[nama]     = []

for _ in range(M):
    a, b = input().split()
    graph[a].append(b)
    graph[b].append(a)

# ambil node dengan heuristik terkecil 
def ambil_terkecil(open_list):
    minimum = 0
    for i in range(len(open_list)):
        if open_list[i][0] < open_list[minimum][0]:
            minimum = i
    return open_list.pop(minimum)

start, goal= input().split()
# algoritma greedy bfs
def greedy_bfs():
    open_list  = [(heuristik[start], start, [start])]
    visited    = []
    dalam_open = [start]
    # lakukan pencarian hingga open_list kosong
    while open_list:
        h, node, rute = ambil_terkecil(open_list)
        # jika node yang diambil adalah goal, kembalikan rute
        if node == goal:
            return rute
        visited.append(node)
        # perikasa tetangga dari node yang diambil
        for tetangga in graph[node]:
            if tetangga not in visited and tetangga not in dalam_open:
                open_list.append(
                    (heuristik[tetangga], tetangga, rute + [tetangga]))
                dalam_open.append(tetangga)
    return None

# jalankan output
rute = greedy_bfs()
if rute:
    print(" -> ".join(rute))
else: #jika rute tidak ditemukan 
    print("TIDAK ADA") 