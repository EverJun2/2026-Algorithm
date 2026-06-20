from collections import deque

def solution(priorities, location):
    q = deque()
    answer = 0
    
    for i in priorities : 
        q.append(i)
    
    while q :
        temp = q.popleft()
        location -= 1 
        if check(temp, q) : 
            answer += 1
            if location == -1 : break
        else : 
            q.append(temp) 
            if location == -1 : location = len(q)-1
        
    
    return answer

def check(temp, q) :
    for i in q :
        if temp < i : return False
    return True
