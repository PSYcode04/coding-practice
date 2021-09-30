# 프로그래머스 60057 (2020 카카오 신입공채)

string = input()


def solution(s):
    answer = len(s)

    # cut 자르는 단위
    for cut in range(1, len(s) // 2 + 1):
        new_str = ""  # 압축하는 문자열 저장
        count = 1  # 반복된 개수
        cut_str = s[0:cut]  # 시작 문자열
        for _next in range(cut, len(s), cut):  # 자르는 단위만큼 점프
            # 시작 문자열이랑 같으면 cut
            if cut_str == s[_next:cut+_next]:
                count += 1  # 자른 개수 추가
            else:  # 시작 문자열이랑 다르면 이전까지 자른 문자열 업데이트
                if count >= 2:  # count가 1이 아니면 업데이트
                    new_str += str(count) + cut_str # 문자열 새로
                else:
                    new_str += cut_str
                cut_str = s[_next:cut + _next]  # 자르는 문자열 새로 등록
                count = 1  # 다시 초기화

        # 남은 문자열 추가
        new_str += str(count) + cut_str if count >= 2 else cut_str
        answer = min(answer, len(new_str))

    return answer


print(solution(string))