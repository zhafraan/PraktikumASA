def caripermen(A,T):
    kotak = len(A)
    permen =[] #menyimpan semua kombinasi yang memenuhi

    def backtrack(i, current, choice):
        #jika jumlahnya sudah sesuai dengan target,simpan ke permen
        if current == T:
            permen.append(list(choice))
            return
        #jika jumlah lebih dari teget maka tidak di lanjutkan
        if current > T or i >= kotak:
            return
        #pilih A[i] tambah elemen ke kombinasi dan lanjutkan ke elemen berikutnya
        choice.append(A[i])
        backtrack(i + 1, current + A[i], choice)
        choice.pop()
        #tidak memilih A[i] dan lanjutkan ke elemen berikutnya
        backtrack(i + 1, current, choice)

    backtrack(0, 0, [])
    return permen

N,T = map(int, input().split())
A = list(map(int, input().split()))
if caripermen(A,T):
    print("YES")
else:
    print("NO")