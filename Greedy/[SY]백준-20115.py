n = int(input())
drink = list(map(int, input().split()))
result = 0

drink.sort()

for i in range(n-1):
    result += drink[i] / 2

result += drink[n-1]
print(result)