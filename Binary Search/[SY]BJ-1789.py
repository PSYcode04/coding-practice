S = int(input())

start = 1
end = S

while start <= end:
    mid = (start + end) // 2
    # 만약 start~mid까지의 합이 200보다 크면 mid를 줄인다.
    # start~mid 까지의 합이 200보다 작으면 answer에 입력한다. 최대값을 구한다.
    if (mid*(mid+1)) // 2 > S:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)