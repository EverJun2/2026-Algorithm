def solution(array, commands):
    answer = []
    
    for i in range(0, len(commands)) :
        start = commands[i][0]-1
        end = commands[i][1]
        
        temp = array[start:end]
        temp.sort()
        
        inx = commands[i][2]-1
        answer.append(temp[inx])
  
    return answer