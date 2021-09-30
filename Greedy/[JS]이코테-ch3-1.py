n=1260

coins = [500, 100, 50, 10]
count = 0

for coin in coins:
  count+=n//coin
  n=n%coin

print(count)