n = int(input())    # 도시 개수
length = list(map(int, input().split()))    # 각 도시 사이 거리 (순서대로)
price = list(map(int, input().split()))     # 각 도시의 주유소 가격 (순서대로)
min_price = price[0]    # 최소 가격 (최소가격이면 그 가격만큼 더함)
result = 0  # 전체 기름 값

# 마지막 주유소는 상관없음
for i in range(n-1):
    # 해당 주유소가 최소 가격보다 작으면 해당 값으로 최소 값 변경
    if price[i] < min_price:
        min_price = price[i]

    result += min_price * length[i] # 이동할 거리만큼 충전

print(result)
