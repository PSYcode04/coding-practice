n = int(input())
time = list(map(int, input().split()))

time.sort()
result = 0

for i in range(n):
    result += time[i] * (n-i)
print(result)