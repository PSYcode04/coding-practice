s = input()
s = list(s)
s = list(map(int, list(s)))
len_s = len(s)

total=0

for i in range(len_s):
  if s[i]!=0 and total!=0:
    total*=s[i] 
  else:
    total+=s[i]

print(total)