zero2one=0
one2zero=0

s=list(map(int, list(input())))

if s[0]==1:
  one2zero+=1
else:
  zero2one+=1

# zero2one
for i in range(len(s)-1):
  if s[i] != s[i+1]:
    if s[i+1]==1:
      one2zero+=1
    else:
      zero2one+=1

print(min(one2zero, zero2one))
  