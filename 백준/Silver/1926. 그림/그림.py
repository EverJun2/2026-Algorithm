a, b = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(a)]
moveX = [0, 0, -1, 1]
moveY = [-1, 1, 0, 0]
check = [[0]*b for _ in range(a)]
cnt = 0
ans = 0

def S1926():
    global cnt, ans
    for i in range (a) :
        for j in range (b) :
            if arr[i][j] == 1 and check[i][j] == 0 :
                cnt += 1
                ans = max(dfs(i,j), ans)
   
    print(cnt)
    print(ans)
    
    return 

def dfs(x , y):
    cnt = 1
    check[x][y] = 1
    queue = list()
    queue.append([x,y])

    while queue :
        x, y = queue.pop()
        for i in range (4) :
            nx = moveX[i] + x
            ny = moveY[i] + y

            if nx >= 0 and nx < a and ny >= 0 and ny < b and check[nx][ny] == 0:
                if arr[nx][ny] == 1 :
                    queue.append([nx,ny])
                    check[nx][ny] = 1
                    cnt += 1

    return cnt



S1926()