# input
n = int(input())
# base case
if n <= 1: 
    print(n)
else:
    # bottom up dp
    C = [0] * (n + 1)
    # base case
    C[0] = 0 
    C[1] = 1   
    i = 2
    while i <= n: #relasi rekurens 
        C[i] = C[i - 1] + C[i - 2]
        i = i + 1
    print(C[n])