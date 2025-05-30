line1=input()
n = int(line1)
initial_queue = [int(x) for x in input().split()]
matris = []
for _ in range(n):
    matris.append([int(x) for x in input()])

visited = ["white"] * n
components = []
o=0
for j in range(n):
    if visited[j]=="white" and o==0:
        q = []
        stack = [j]
        while stack:
            v = stack.pop()
            if  visited[v]== "white" and o==0:
                visited[v] = "black"
                o=0
                q.append(v)
            for i in range(n):
                if matris[v][i] == 1 and visited[i]=="white" and o==0:
                    stack.append(i)
                    o=0
                      
        components.append(q)

javab = initial_queue[:]
k=0
for k in range(len(components)):
    values = []
    for i in components[k]:
        values.append(initial_queue[i])

    values.sort()
    sobjects = sorted(components[k])
    for i in range(len(sobjects)):
        javab[sobjects[i]] = values[i]

print(*javab)
