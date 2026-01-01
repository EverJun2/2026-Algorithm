def S9012():
    num = int(input())
    for i in range(num):
        stack = []
        arr = input()
        for j in arr:
            if j == '(' : stack.append(j)
            elif j == ')' : 
                if stack:
                    stack.pop()
                else: 
                    print("NO")
                    break
        else:
            if not stack: print("YES")
            else: print("NO")
    
    return 0

S9012()