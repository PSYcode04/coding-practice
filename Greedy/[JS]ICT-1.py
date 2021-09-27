n=int(input())

person = list(map(int, input().split()))
person.sort(reverse=True)

i=0
count=0

while True:
  i=i+person[i]
  count+=1
  
  if i==n or i >n:
    break

print(count)






