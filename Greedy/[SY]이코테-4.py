n = int(input())
coin = list(map(int, input().split()))
coin.sort() # 오름차순 정렬
result = 1  # 가장 작은 양의 정수

for _coin in coin:
    if result < _coin:
        break
    result += _coin

print(result)