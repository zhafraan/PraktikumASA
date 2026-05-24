import heapq
#pakai djikstra untuk mencari jarak terpendek dari node S ke T 
def dijkstra(graph, start, n):
    dist = {node: float('inf') for node in range(1, n + 1)}#inisialisasi jarak semua node ke infinity
    dist[start] = 0 #jarak node awal ke sendiri adalah 0
    queue = [(0, start)]#buat menyimpan node yang akan diproses, dengan jarak terpendek saat ini

    while queue:
        current_dist, current_node = heapq.heappop(queue)#ambil node dengan jarak terpendek saat ini
        #lewati jika jarak yang diambil lebih besar dari jarak yang sudah diketahui untuk node tersebut
        if current_dist > dist[current_node]:
            continue
        #cek tetangga dari node saat ini dan perbarui jarak jika ditemukan yang lebih pendek
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:#jarak baru lebih pendek, perbarui jarak dan tambahkan ke antrian
                dist[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return dist

def antarpaket():
    N,M = map(int, input().split())
    graph = {i: [] for i in range(1, N + 1)} #inisialisasi graph 
    for _ in range(M):#input untuk setiap edge, dengan dari node a ke node b dengan bobot c
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    #untuk node S ke tujuan T, pakai dijkstra untuk mencari jarak terpendek dari S ke T
    S,T = map(int, input().split())
    hasil = dijkstra(graph, S, N)
    if hasil[T] == float('inf'):
        print(-1)
    else:
        print(hasil[T])
antarpaket()