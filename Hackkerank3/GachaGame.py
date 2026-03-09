N, X = map(int, input().split())
T1 = [0]*N
T2 = [0]*N

def bacaInput(i):
    if i == N:
        return
    a, b = map(int, input().split())
    T1[i] = a
    T2[i] = b
    bacaInput(i+1)   
bacaInput(0)
batas = 10**9

def TargetSSR(i, p, ssr):
    if ssr >= X:
        return 0
    if i == N:
        return batas
    # pilihan mesin 1
    if p >= T1[i]-1:
        r1 = 1 + TargetSSR(i+1, 0, ssr+1)
    else:
        r1 = 1 + TargetSSR(i+1, p+1, ssr)
    # pilihan mesin 2
    if p >= T2[i]-1:
        r2 = 1 + TargetSSR(i+1, 0, ssr+1)
    else:
        r2 = 1 + TargetSSR(i+1, p+1, ssr)

    if r1 < r2:
        return r1
    else:
        return r2

hasil = TargetSSR(0, 0, 0)
if hasil > N:
    print(-1)
else:
    print(hasil)