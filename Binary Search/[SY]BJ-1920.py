n = int(input())    # 정수 배열 원소 수
array = list(map(int, input().split()))

m = int(input())    # 체크할 숫자 수
isCheck = list(map(int, input().split()))

array.sort() # 이진 탐색을 위해서 탐색할 배열 정렬


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2    # 중간점 인덱스
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


for num in isCheck:
    print(binary_search(array, num, 0, n-1))



