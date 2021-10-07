n = int(input())

level = 1
last_room = 1

while n > last_room:
    last_room += level * 6
    print(last_room)
    level += 1

print(level)