def S10773():
    num = int(input())
    stack = []

    for i in range(num) :
        temp = int(input())
        if temp == 0 : stack.pop()
        else : stack.append(temp)
    sum = 0
    for i in stack :
        sum += i
    print(sum)
    return 0

S10773()