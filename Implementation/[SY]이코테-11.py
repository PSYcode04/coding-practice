n = int(input())    # 보드 크기
k = int(input())    # 사과 개수

# (n+2) * (n+2) 크기의 보드판을 만들고
# 테두리 (0,0) ~ (0,n+2), (n+2, 0) ~ (n+2, n+2), (1, 0) ~ (n+1, 0), (1, n+2) ~ (n+1, n+2) 는 2
# 사과 있는 부분은 1
# 나머지 이동 가능한 부분은 0

board = [[0] * (n+2) for _ in range(n+2)]

# 사과 위치
for apple in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1

# 방향 변환 정보
L = int(input())
direction = []
for d in range(L):
    x, c = map(str, input().split())
    direction.append((int(x), c))

# 테두리
for i in range(n+1):
    board[0][i] = 2
    board[i][n+1] = 2
    board[n+1][i+1] = 2
    board[i+1][0] = 2

# 첫 이동은 오른쪽
x, y =1, 1  # 뱀의 머리 시작 좌표
board[x][y] = 3 # 뱀의 몸은 3
length = 1  # 뱀의 길이
time = 0 # 걸린 시간
dx = 0
dy = 1
# 이동한 방향 기록할 배열
save = [(1, 1)]
dir_index = 0   # 방향 관련 인덱스

# 이제 시뮬레이션 구현
# 뱀은 (1, 1) 위치에서 출발
while True:
    check = False
    time += 1   # 시간 증가
    # 다음 뱀의 머리가 위치할 곳의 상태 확인 (다음 머리 좌표)
    nx = x + dx
    ny = y + dy

    # 사과가 있다면
    if board[nx][ny] == 1:
        length += 1 # 몸 길이 증가
        save.append((x, y)) # 꼬리부분 추가
    elif board[nx][ny] == 0:    # 아무것도 아니면
        check = True    # 꼬리 삭제
    elif board[nx][ny] == 2 or board[nx][ny] == 3:   # 벽이거나 자기 몸을 만나면
        print(time)
        break

    save.insert(0, (nx, ny))
    # 머리 좌표
    x = nx
    y = ny

    index = 0
    # 길이만큼 이동
    for i in range(length):
        board[save[i][0]][save[i][1]] = 3
        index = i
    if check:
        board[save[index+1][0]][save[index+1][1]] = 0
    del save[index+1:]

    # 이동 방향 체크
    if dir_index < len(direction) and direction[dir_index][0] == time:  # 방향 전환할 시간이라면
        if direction[dir_index][1] == 'L':
            if dx == 0:
                if dy == 1:
                    dx = -1
                    dy = 0
                elif dy == -1:
                    dx = 1
                    dy = 0
            elif dx == 1:
                dx = 0
                dy = 1
            elif dx == -1:
                dx = 0
                dy = -1
        elif direction[dir_index][1] == 'D':
            if dx == 0:
                if dy == 1:
                    dx = 1
                    dy = 0
                elif dy == -1:
                    dx = -1
                    dy = 0
            elif dx == 1:
                dx = 0
                dy = -1
            elif dx == -1:
                dx = 0
                dy = 1
        dir_index += 1