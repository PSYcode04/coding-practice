n = int(input())
tip = []
result = 0

for i in range(n):
    tip.append(int(input()))


# 무조건 원래 주려고 한 팁에서 index 를 뺀 값을 준다.
tip.sort(reverse=True)
for i in range(n):
    if tip[i] - i < 0:
        break

    result += tip[i]-i

print(result)