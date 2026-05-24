# input
n, a, b = map(int, input().split())

# base case
if n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    # bottom up dp
    M = [0] * (n + 1)
    # inisialisasi nilai base case
    M[0] = a
    M[1] = b
    i = 2
    while i <= n:
        M[i] = M[i - 1] + M[i - 2]# relasi rekurens
        i = i + 1
    print(M[n])