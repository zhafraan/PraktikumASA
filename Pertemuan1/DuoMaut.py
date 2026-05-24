n = int(input())
arr = list(map(int, input().split()))

max_power= 0
for i in range(n):
    for j in range(i+1, n):
        total = arr[i]+arr[j]
        if total > max_power:
            max_power = total
        
print(max_power)