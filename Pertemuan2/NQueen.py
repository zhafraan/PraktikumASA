n = int(input())
kolom = [False] * n
D1 = [False] * (2 * n)
D2 = [False] * (2 * n)
posisi = [0] * n

def Hasilkan(baris):
    if baris == n:
        for i in range(n):
            baris_str = ""
            for j in range(n):
                if j == posisi[i]:
                    baris_str += 'Q'
                else:
                    baris_str += '.'
            print(baris_str)
        return True
    for k in range(n):
        if not kolom[k] and not D1 [baris - k + n] and not D2[baris + k]:
            kolom[k] = D1[baris - k + n] = D2[baris + k] = True
            posisi[baris] = k
            if Hasilkan(baris + 1):
                return True
            kolom[k] = D1[baris - k + n] = D2[baris + k] = False
    return False

if not Hasilkan(0):
    print("Kerajaan tidak dapat dilindungi!")