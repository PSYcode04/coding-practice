n = int(input())
product = []
result = 0

for i in range(n):
    product.append(int(input()))

# 비싼거 순서대로 정렬
product.sort(reverse=True)

# 묶이지 않는 나머지 제품 개수
remain = len(product) % 3

for i in range(0, n-remain, 3):
    result += product[i] + product[i+1]

# 나머지 더하기
for i in range(remain):
    result += product[n-i-1]

print(result)

