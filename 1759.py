from itertools import combinations

vowel = set('aeiou')
def is_valid(password):
    vowelCnt = sum(1 for char in password if char in vowel)
    count = len(password) - vowelCnt
    return vowelCnt >= 1 and count >= 2

L, C = map(int, input().split())
chars = sorted(input().split())

for comb in combinations(chars, L):
    password = ''.join(comb) 
    if is_valid(password): 
        print(password)  