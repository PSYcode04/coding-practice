food_times = list(map(int, input().split()))
k = int(input())
temp = 0
count = 0
food = 0
t = 0

print(food_times, k)

while temp != -1:    

  food = food % len(food_times)

  if t == k:
    temp = food+1
    break;
    
  if food_times[food] != 0:
    food_times[food] -= 1
    food += 1
    t += 1
    
  else: 
    count += 1
    food += 1 # 배열의 0인 수 셈
    # food_times == 0 이면 건너뜀 # 시간 증가 안 함

  # 종료 조건
  if food == len(food_times): # 배열 
    if count == len(food_times): 
      temp = -1
  
    else:
      count = 0
  

print(temp)