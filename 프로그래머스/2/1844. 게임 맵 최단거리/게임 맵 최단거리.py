from collections import deque

def solution(maps):
    answer = 0
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    answerArr = []
        
    # 상하좌우
    arrX = [-1, 1, 0, 0]
    arrY = [0, 0, -1, 1]
    
    q = deque()
    
    
    def bfs(x, y) :
        q.append([x,y,1])
        visited[x][y] = True
        
        while q :
            loc = q.popleft()
            locX = loc[0]
            locY = loc[1]
            dist = loc[2]
            if locX == len(maps)-1 and locY == len(maps[0])-1 : return dist
            for i in range(4):
                nextX = locX + arrX[i]
                nextY = locY + arrY[i]
                
                if nextX >= 0 and nextX < len(maps) and nextY >= 0 and nextY < len(maps[0]) :
                    if not visited[nextX][nextY] and maps[nextX][nextY] == 1:
                        visited[nextX][nextY] = True
                        q.append([nextX,nextY,dist+1])
                        
        return -1
    
    answer = bfs(0,0)    
    
    return answer