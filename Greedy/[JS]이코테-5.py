## my_code

# n, m = map(int, input().split())
# ball = list(map(int, input().split()))
# ball.sort()
# ball.append(-1) # 마지막 count 빼주기 위해서 넣음

# print(ball)

# total = n*(n-1)/2 # 볼링공으로 만들 수 있는 총 조합 수

# count = 1

# for i in range(len(ball)-1):
#   print('i',i)
  
#   if ball[i] == ball[i+1]: # 같은 수 개수 세서 
#     count += 1
#     print('count',count)
#   else:
#     total -= count*(count-1)/2 # 같은 수 조합 빼줌
#     count = 1

# total = int(total)

# print(total)

## book-code
n, m = map(int, input().split())
data = list(map(int, input().split()))
array=[]

for x in data:
  array[x] += 1 # index : ball 개수 count

result = 0

for i in range(1, m+1):
  n-=array[i] # i 볼링공 개수 제외 
  result += array[i]*n 
  # 1번 공  * (2, 3번 공)
  # 2번 공 * (3번 공) 

  print(result)

