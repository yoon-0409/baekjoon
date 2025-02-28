n = int(input())
phone = list(map(int, input().split()))
last = 0
battery = 0
mul = 2
for i in phone:
    if(last == i):
        mul = mul*2
        battery += mul
    else:
        mul = 2
        battery += 2
    if(battery >= 100) :
        battery = 0
        last = 0
        continue
    last = i
    # print(i,battery)
print(battery)