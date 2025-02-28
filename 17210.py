door = int(input())
first = int(input())
if first == 1:
    first = True
else:
    first = False
if door > 5:
    print("Love is open door")
else:
    for i in range(door-1):
        first = not first
        print(int(first))
