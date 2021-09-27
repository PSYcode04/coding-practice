# 프로그래머스 60057 (2020 카카오 신입공채)

key_input = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock_input = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def rotate(a):
    n = len(a)  # 2차원 배열 행
    m = len(a)  # 2차원 배열 열
    new_array = [[0] * m for _ in range(n)]

    for row in range(n):
        for col in range(m):
            new_array[col][n-row-1] = a[row][col]

    return new_array


def check_lock(a):
    n = len(a) // 3
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if a[i][j] != 1:
                return False    # 자물쇠를 풀지 못함

    return True


def solution(key, lock):

    m = len(key)     # key의 크기
    n = len(lock)    # lock의 크기 (m <= n)

    expand_lock = [[0] * (3*n) for _ in range(3*n)] # 새로운 배열

    # 새로운 배열의 자물쇠 위치에 자물쇠 입력
    for i in range(n):
        for j in range(n):
            expand_lock[n+i][n+j] = lock[i][j]

    # 4방향으로 돌리면서 자물쇠 전체를 열쇠로 확인하기
    for i in range(4):
        # 자물쇠 전체 탐색
        # 3배 확장한 상태니까 시작위치만 생각해서 범위가 2*n
        for lock_row in range(2*n):
            for lock_col in range(2*n):
                # key 넣기
                for key_row in range(m):
                    for key_col in range(m):
                        expand_lock[lock_row+key_row][lock_col+key_col] += key[key_row][key_col]

                # 원래 자물쇠 부분 홈(0)이 다 채워졌는지(1) 확인
                if check_lock(expand_lock):
                    return True
                else:   # 다시 원상태로 복구
                    for key_row in range(m):
                        for key_col in range(m):
                            expand_lock[lock_row + key_row][lock_col + key_col] -= key[key_row][key_col]

        key = rotate(key)
    return False


print(solution(key_input, lock_input))