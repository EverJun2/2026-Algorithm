def solution(numbers, target):
    answer = 0
    answer = dfs(target, numbers, 0, 0, answer)
    return answer

def dfs(target, numbers, index, sume, cnt) :
    if index == len(numbers):
        if sume == target : 
            cnt += 1
        return cnt
    
    cnt1 = dfs(target, numbers, index+1, sume + numbers[index], cnt)
    cnt2 = dfs(target, numbers, index+1, sume - numbers[index], cnt)
    return cnt1 + cnt2