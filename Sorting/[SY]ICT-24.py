n = int(input())
house = list(map(int, input().split()))
house.sort()    # 정렬

if n % 2 == 1:
    print(house[n//2])
else:
    print(house[n//2 - 1])