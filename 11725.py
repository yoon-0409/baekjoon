N = int(input())   
node = {}
parent = [0] * (N+1)
queue = []

for i in range(1, N+1):
    node[i] = []
    
for _ in range(N-1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

queue.append(1)
while queue:
    cur = queue.pop(0)
    for i in node[cur]:
        if parent[cur] == i:
            continue
        parent[i] = cur
        queue.append(i)
    
for i in range(2, N+1):
    print(parent[i])