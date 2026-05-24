string = input()

def Cek(Input, jmlXY):
    if len(Input) < 2 and jmlXY == 0:
        print(False)
    else:
        potong = Input[0:2]
        if potong == "XY":
            jmlXY += 1
        if len(Input) == 1:
            print(jmlXY % 2 == 0)
        else:
            Cek(Input[1:], jmlXY)

Cek(string, 0)