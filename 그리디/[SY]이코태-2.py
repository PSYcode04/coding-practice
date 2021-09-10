s = input()

# 연산자 우선순위 관계 없이 왼쪽부터 순서대로 계산

# result 혹은 현재 숫자가 0이면 '+' 연산
# 둘 중 하나라도 1이라면 '+' 연산

result = 0

for num in s:
    if result == 0 or int(num) == 0:
        result += int(num)
    elif result == 1 or int(num) == 1:
        result += int(num)
    else:
        result *= int(num)

print(result)
