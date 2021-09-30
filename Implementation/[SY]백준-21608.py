N = int(input())

room = [[0] * N for _ in range(N)]      # N*N 개로 자리 생성
mate = [[0] * 4 for _ in range(N*N)]    # 선호하는 학생 입력받을 공간
student = [0] * (N*N)                   # 학생 순서 입력

# 인접한 부분 좌표 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0  # 만족도

# 학생 수 만큼 좋아하는 학생 4명씩 입력받아서 리스트에 추가하기
# mate[i]: 숫자가 mate[i][0]인 학생이 좋아하는 학생 4명을 mate[i][1] 부터
for i in range(N*N):
    arr = list(map(int, input().split()))
    student[i] = arr[0]
    mate[i] = arr[1:]

# 학생 수 만큼 room 탐색하면서 위치 찾기
for _student in student:
    # 학생 자리 지정
    select_x = 0
    select_y = 0

    max_love = -1    # 좋아하는 학생 수 최대
    max_blank = -1   # 빈 자리 수 최대

    # _student 학생의 자리 찾기
    # 행 이동
    for i in range(N):
        # 열 이동
        for j in range(N):

            if room[i][j] == 0:     # 빈자리인지 확인
                x = i
                y = j
                blank = 0
                love = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or ny < 0 or nx >= N or ny >= N:    # 공간 벗어나는 경우 제외
                        continue

                    if room[nx][ny] == 0:
                        blank += 1  # 빈 자리수 업데이트
                    elif room[nx][ny] in mate[student.index(_student)]:     # 좋아하는 학생에 속하면
                        love += 1   # 좋아하는 학생 업데이트

                # 가장 적절한 자리 좌표 저장
                if max_love < love or (max_love == love and max_blank < blank):
                    select_x = i
                    select_y = j
                    max_love = love
                    max_blank = blank

    room[select_x][select_y] = _student # 선택한 자리에 학생 넣기

# 만족도 구하기
for i in range(N):
    for j in range(N):
        x = i
        y = j
        num = 0     # 좋아하는 학생 수

        # 상, 하, 좌, 우에 위치한 학생이 좋아하는 학생에 속하는지 확인
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:  # 공간 벗어나는 경우 제외
                continue

            if room[nx][ny] in mate[student.index(room[i][j])]:
                num += 1

        if num == 0:
            result += 0
        elif num == 1:
            result += 1
        elif num == 2:
            result += 10
        elif num == 3:
            result += 100
        else:
            result += 1000

print(result)
