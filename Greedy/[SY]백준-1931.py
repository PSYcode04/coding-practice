n = int(input())
time = []
result = 1

for i in range(n):
    start, end = map(int, input().split())
    time.append((start, end))

# 특정 요소를 기준으로 정렬하기
# x[1]로 먼저 정렬하고, 같으면 x[0] 기준?
# reverse 없으면 오름차순, reverse=True이면 내림차순
time = sorted(time, key=lambda x: (x[1], x[0]))
end_time = time[0][1]   # 회의가 가장 빨리 끝나는 회의의 끝나는 시간

for i in range(1, n):
    if end_time <= time[i][0]:
        end_time = time[i][1]
        result += 1

print(result)
