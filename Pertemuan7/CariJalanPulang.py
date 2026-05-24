#ini untuk bagian dfs
def dfs(graph, node, start, visited):
    for neighbour in graph[node]:
        if neighbour == start:
            return True
        if neighbour not in visited:
            visited.add(neighbour)
            if dfs(graph, neighbour, start, visited):
                return True
    return False
# buat menemukan jalurnya menuju lokasi awal yaitu ke S
def temukanjalur():
    N, M, S = map(int, input().split())
    #buat graph
    graph = {}
    for i in range(1, N + 1):
        graph[i] = []
    #buat cabang
    for j in range(M):
        A, B = map(int, input().split())
        graph[A] = graph[A] + [B]
    #visited untuk node yang udah dikunjungi
    visited = set()
    visited.add(S)
    #cari jalur menuju lokasi awal apakah bisa kembali ke S
    jalur_ditemukan = dfs(graph, S, S, visited)
    if jalur_ditemukan:
        print("YES")
    else:
        print("NO")
temukanjalur()