n, m = map(int, input().split())    # n: 전구 개수, m: 명령어 개수
light = list(map(int, input().split())) # 전구 상태

for i in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        light[b-1] = c
    elif a == 2:
        for j in range(c-b+1):
            if light[b-1+j] == 0:
                light[b-1+j] = 1
            else:
                light[b-1+j] = 0
    elif a == 3:
        for j in range(c-b+1):
            light[b-1+j] = 0
    else:
        for j in range(c-b+1):
            light[b-1+j] = 1

for status in light:
    print(status, end=' ')