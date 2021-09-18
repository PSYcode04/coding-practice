octal = input()
binary = ""

# 8진수 한자리는 2진수의 세자리로 변환
# 나머지와 몫

# 첫번째 자리수 변환
first = int(octal[0])
for i in range(2):
    (q, r) = divmod(first, 2)
    first = q
    if q == 0:
        binary = str(r) + binary
        break
    elif q == 1:
        binary = str(q) + str(r) + binary
        break
    else:
        binary = str(r) + binary

# 나머지 변환
for i in range(1, len(octal)):
    number = int(octal[i])
    result = ""
    for div in range(2):
        (q, r) = divmod(number, 2)
        number = q
        if div == 0:
            result += str(r)
        elif div == 1:
            result = str(q) + str(r) + result
    binary += result

print(binary)