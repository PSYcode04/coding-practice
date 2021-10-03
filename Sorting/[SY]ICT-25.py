n = int(input())    # 스테이지 개수
_stages = list(map(int, input().split()))   # 게임을 이용하는 사용자가 현재 멈춰있는 스테이지 번호가 담긴 배열


def solution(N, stages):
    answer = []

    clear = [0] * (N + 1)
    reach = [0] * (N + 1)
    fail = []
    reach_count = 0   # 숫자
    clear_count = 0
    # 1번 스테이지 = 1번 index
    # 각 스테이지를 클리어/도달한 플레이어 수 저장
    for i in range(1, N+1):
        reach_count += stages.count(i-1)
        clear_count += stages.count(i)
        reach[i] = len(stages) - reach_count
        clear[i] = len(stages) - clear_count

    # 실패율 저장
    for i in range(1, N + 1):
        if reach[i] == 0:
            fail.append((i, 0))  # 도달한 플레이어가 없으면 0 그대로
        else:
            fail_rate = (reach[i] - clear[i]) / reach[i]
            fail.append((i, fail_rate))

    fail.sort(key=lambda x: -x[1])

    for i in range(N):
        answer.append(fail[i][0])

    return answer


print(solution(n, _stages))