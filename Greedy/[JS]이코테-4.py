n=int(input())
data = list(map(int, input().split()))
data.sort() # 작은 순으로 배열 

target = 1

for x in data : 
  if target < x : 
    break
  target += x

print(target)