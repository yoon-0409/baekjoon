N,M,K = map(int,input().split())

c = N - M*K
print( c if c > 0 else 0 , c + M - 1) 