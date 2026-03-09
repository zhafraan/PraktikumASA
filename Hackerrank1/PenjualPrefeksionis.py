n = int(input())
a = list(map(int, input().split()))

minimum = -1
for kualitas in range(min(a), max(a) + 1):
    total = 0
    for barang in a:
        total += abs(barang - kualitas)
    if minimum == -1 or total < minimum:
        minimum = total

print(minimum)