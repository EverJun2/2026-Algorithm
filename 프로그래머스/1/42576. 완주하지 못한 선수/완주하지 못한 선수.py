def solution(participant, completion):
    answer = ''
    cnt = {}
    
    for p in participant :
        if p in cnt : cnt[p] += 1
        else : cnt[p] = 1
    
    for c in completion : 
        if c in cnt : cnt[c] -= 1

    for name in cnt : 
        if cnt[name] > 0 : answer += name
    return answer