# menggunakan iterative dfs untuk cari tumbler 
def iterative(P, start):
    visited = set()
    stack = [start]
    # untuk menyimpan posisi yang udah dikunjungi pake stack
    while stack:
        posisi = stack[len(stack) - 1]
        stack = stack[:len(stack) - 1]
        if posisi in visited:
            return posisi
        visited.add(posisi)
        stack = stack + [P[posisi]]
 
def caritumbler(P, j, N):
    if j > N:
        return
    print(iterative(P, j))
    caritumbler(P, j + 1, N)

def hasil():
    N = int(input())
    data = list(map(int, input().split()))
    # untuk menyimpan posisi dan nilai P
    P = {}
    # isi nilai P sesuai dengan inputnya
    for i in range(1, N + 1):
        P[i] = data[i - 1]
    # cari tumbler yang akan kembali ke posisi awal
    caritumbler(P, 1, N)
hasil()