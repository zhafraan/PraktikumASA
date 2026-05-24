# input
N, M = map(int, input().split())
# untuk menyimpan nilai heuristik dan graph
heuristik = {}
graph     = {}
for i in range(N):
    nama, h = input().split()
    heuristik[nama] = int(h)
    graph[nama] = []
for _ in range(M):
    a, b = input().split()
    graph[a].append(b)
    
start, goal = input().split()
# ambil node dengan heuristik terkecil
def ambil_terkecil(open_list):
    minimum = 0
    for i in range(len(open_list)):
        if open_list[i][0] < open_list[minimum][0]:
            minimum = i
    return open_list.pop(minimum)

# algoritma greedy bfs
def greedy_bfs():
    open_list  = [(heuristik[start], start, [start])]
    visited    = []
    dalam_open = [start]
    diperiksa  = 0  # buat jumlah node yang diperiksa
    # lakukan pencarian hingga open_list kosong
    while open_list:
        h, node, rute = ambil_terkecil(open_list)
        diperiksa = diperiksa + 1 
        # jika node yang diambil goal ,maka kembalikan rute dan jumlah diperiksa
        if node == goal:
            return rute, diperiksa
        visited.append(node)
        # periksa tetangga dari node yang diambil
        for tetangga in graph[node]:
            if tetangga not in visited and tetangga not in dalam_open:
                open_list.append(
                    (heuristik[tetangga], tetangga, rute + [tetangga]))
                dalam_open.append(tetangga)
    return None, diperiksa

# jalankan output
rute, diperiksa = greedy_bfs()
if rute:
    print(" -> ".join(rute))
else:
    print("TIDAK ADA")
print("DIPERIKSA: " + str(diperiksa))