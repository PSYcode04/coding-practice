s = input()

# 전체 문자열에서 알파벳 리스트, 숫자 리스트로 각각 나눈다.

alpha = list()
num = list()

for char in s:
    if char.isalpha():
        alpha.append(char)
    else:
        num.append(int(char))

alpha.sort()    # 알파벳 리스트 오름차순 정렬

# 출력
for i in range(len(alpha)):
    print(alpha[i], end='')

result = 0
for i in range(len(num)):
    result += num[i]
print(result)   # 숫자 합 출력
