N,K = map(int, input().split())
G = list(map(int, input().split()))

def petiharta(peti,emas):
    if emas > K :
        return 0
    if peti == N:
        return emas
    A = petiharta(peti + 1, emas + G[peti])
    B = petiharta(peti+1, emas) 
    
    if A > B :
        return A
    else :
        return B
    
print(petiharta(0,0))