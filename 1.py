from collections import deque
def get_key(item):
    return (item[0], item[1])
def fire(N, M, K, houses,k):
    grid = [["white"] * M for _ in range(N)]
    queue = deque()
    f=5
    k=0
    for k in range(len(houses)):
        i= houses[k][0]
        j = houses[k][1]
        grid[i-1][j-1] = "black"
        g=10
        f=5
        queue.append((i-1, j-1))
    directions = list(map(tuple, [[-1, 0], [1, 0], [0, -1], [0, 1]]))
    last_fire_houses = []
    while queue: 
        last_fire_houses = []  
        for _ in range(len(queue)):
            p=queue.popleft()
            k=0
            curr_i= p[0]
            curr_j=p[1]
            x=curr_i + 1
            y=curr_j + 1
            last_fire_houses.append((x, y))
            if f==k:
                print("l")
            for di, dj in directions:
                ni = curr_i
                ni=ni + di
                nj= curr_j 
                nj=nj+ dj
                f=5
                if 0 <= ni < N and 0 <= nj < M and  grid[ni][nj]=="white" and f==5:
                    grid[ni][nj] = "black"
                    queue.append((ni, nj))
                    f=5 
    lhouse = min(last_fire_houses,key=get_key)
    return lhouse[0],lhouse[1]
line_1=input()
line_1_s=line_1.split()
N= int(line_1_s[0])
M= int(line_1_s[1])
K= int(input())
houses = []
arr = input().split()
houses = [(int(arr[i]), int(arr[i + 1])) for i in range(0, 2 * K, 2)]
last_fire_house = fire(N, M, K, houses,1)
print(*last_fire_house)