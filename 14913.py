a,b,k = map(int,input().split())

# print(a,b,k)
# n = b - a
cnt = 1
while True:
    if a == k:
        print(cnt)
        break
    elif a > k and b > 0:
        print("X")
        break
    elif a < k and b < 0:
        print("X")
        break
    cnt += 1
    a+=b
    # print(a)
    # input()