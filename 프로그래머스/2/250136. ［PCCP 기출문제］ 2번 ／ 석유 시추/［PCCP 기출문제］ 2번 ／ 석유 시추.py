from collections import deque

def solution(land):
    answer = [0]* len(land[0])
    visited = [[False] * len(land[0]) for _ in range(len(land))]
    
    for i in range(0, len(land)) :
        for k in range(0, len(land[0])) :
            if not visited[i][k] and land[i][k] == 1: 
                temp = bfs(land, answer, i, k, visited)
                
    return max(answer)

def bfs(land, answer, i, k, visited) :
    queue = deque()
    xArr = [-1, 1, 0, 0]
    yArr = [0, 0, -1, 1]
    queue.append([i,k])
    count = 1
    visited[i][k] = True
    
    cols = set()
    cols.add(k)
    
    while queue :
        now = queue.popleft()
        
        for i in range (0,4) : 
            xIdx = now[0] + xArr[i]
            yIdx = now[1] + yArr[i]
            
            if check(xIdx, yIdx, land) : 
                if visited[xIdx][yIdx] != True and land[xIdx][yIdx] == 1 :
                    count+=1
                    cols.add(yIdx)
                    queue.append([xIdx, yIdx])
                    visited[xIdx][yIdx] = True
    for c in cols:
        answer[c] += count     
    return

def check(x, y, land) :
    if 0 <= x < len(land) and 0 <= y < len(land[0]) : return True
    return False

    