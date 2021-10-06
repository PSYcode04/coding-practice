N = int(input())    # 상근이가 가진 숫자 카드 수
card = list(map(int, input().split()))  # 상근의 숫자 카드에 적힌 정수 배열
M = int(input())    # 가지고 있는지 체크할 정수 개수
check = list(map(int, input().split())) # 체크할 정수 배열

card.sort() # 이진 탐색을 위한 정렬

answer = [] # 숫자가 있는지 체크할 배열


def search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


for num in check:
    answer.append(search(card, num, 0, N-1))

for ans in answer:
    print(ans, end=' ')