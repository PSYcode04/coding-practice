from queue import PriorityQueue
# 데이터가 제거될 때 가장 작은 값부터 제거

N = int(input())
que = PriorityQueue()   # 빈 우선순위 큐 초기화
result = 0

for i in range(N):
    que.put(int(input()))

while que.qsize() != 1:
    new_val = que.get() + que.get()
    result += new_val
    que.put(new_val)

print(result)
