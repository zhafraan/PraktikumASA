N, K = map(int, input().split())
op1 = [""] * N
c1 = [0] * N
op2 = [""] * N
c2 = [0] * N

def BacaInput(i):
    if i == N:
        return
    a, b, c, d = input().split()
    op1[i] = a
    c1[i] = int(b)
    op2[i] = c
    c2[i] = int(d)
    BacaInput(i + 1)
# rekursi untuk mencari poin maksimum
def hitung(hari, poin):
    if hari == N:   # basis
        return poin
    if op1[hari] == '+':
        result1 = hitung(hari + 1, poin + c1[hari])
    else:
        result1 = hitung(hari + 1, poin * c1[hari])
    if op2[hari] == '+':
        result2 = hitung(hari + 1, poin + c2[hari])
    else:
        result2 = hitung(hari + 1, poin * c2[hari])
    if result1 > result2:
        return result1      
    else:
        return result2


BacaInput(0)
print(hitung(0, K))