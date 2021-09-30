n = int(input())
afraid = list(map(int, input().split()))    # N 명의 모험가의 각 공포도 입력받기
afraid.sort()   # 공포도가 작은 값부터 정렬
print(afraid)
# 큰 값부터

group = 0   # 그룹 수
index = 0   # 인덱스

# 공포도가 작은 애들부터 그룹 구성하면 그룹 수가 최대가 된다?
while True:
    index += afraid[index]

    # 리스트 인덱스를 넘어가면 남은 인원은 두고간다.
    if index < n - 1:
        group += 1
    else:
        break

print(group)