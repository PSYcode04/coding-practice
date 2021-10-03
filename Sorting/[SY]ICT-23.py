# 백준 10825
n = int(input())
score = []

# 이름, 국어, 영어, 수학
for i in range(n):
    name, k, e, m = map(str, input().split())
    score.append((name, int(k), int(e), int(m)))

# 정렬
score.sort(key=lambda x: ((-x[1]), x[2], (-x[3]), x[0]))

for name in score:
    print(name[0])