t = int(input())

for case in range(t):
    n = int(input())    # 정수 개수
    number = list(map(int, input().split()))
    max_num = max(number)
    min_num = min(number)
    print(min_num, max_num)