s = input() # 문자열 입력
zero2One = 0
one2Zero = 0

if s[0] == '0':
    zero2One += 1
else:
    one2Zero += 1

for i in range(1, len(s)):
    # 값이 바뀌는 경우
    if s[i-1] == '0' and s[i] == '1':
        one2Zero += 1
    elif s[i-1] == '1' and s[i] == '0':
        zero2One += 1

print(zero2One if zero2One < one2Zero else one2Zero)