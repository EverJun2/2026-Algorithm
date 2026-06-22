def solution(clothes):
    hash_map = {}
    
    for temp in clothes :
        hash_map[temp[1]] = hash_map.get(temp[1], 0) + 1
    
    answer = 1
    for count in hash_map.values():
        answer *= (count + 1)  
    return answer - 1
    
    return answer