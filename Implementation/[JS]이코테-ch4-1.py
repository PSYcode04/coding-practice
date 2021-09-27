n = int(input())
direction = list(input().split())

# 방향 벡터 설정
# 행 이동 
dx= [0, 0, 1, -1] # D, U
# 열 이동
dy = [-1, 1, 0, 0] # L, R
dir = ['L', 'R', 'D', 'U']

x, y = 1, 1 

for i in range(len(direction)):
  for j in range(len(dir)):
    if direction[i] == dir[j]:
        nx = x + dx[j]
        ny = y + dy[j]
        print(nx, ny)
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue

  x = nx
  y = ny

print(x, y)
    