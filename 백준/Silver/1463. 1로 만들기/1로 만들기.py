def S1463():

    inp = int(input())

    dp = [-1] * (inp + 1)
    dp[0] = 0
    dp[1] = 0

    if inp >= 2 :
        for i in range (2, inp+1) :
            dp[i] = dp[i - 1] + 1

            if i % 2 == 0:
                dp[i] = min(dp[i], dp[i // 2] + 1)
                
            if i % 3 == 0:
                dp[i] = min(dp[i], dp[i // 3] + 1)
        
    print(dp[inp])
    return

S1463()