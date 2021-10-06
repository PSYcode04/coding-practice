T = int(input())


# 팩토리얼 함수
def factorial(x):
    if x <= 1:
        return 1

    return x * factorial(x-1)


for i in range(T):
    N, M = map(int, input().split())
    result = factorial(M) // (factorial((M-N)) * factorial(N))
    print(result)

