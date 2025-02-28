n = int(input())
sum = 0
for i in range(1,n+1):
    if(i == 1):
        continue 
    elif(i == 2):
        sum+=2
    elif(i%2 == 0):
        sum += i-1
    else:
        sum+=i
    #print(sum)

print(sum)
