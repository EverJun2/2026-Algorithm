def S11726():

    inp = int(input())

    dp = [-1] * (inp + 3)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    if inp >= 3 :
        for i in range (3, inp+1) :
            dp[i] = dp[i-2] + dp[i-1]
            
    print(dp[inp] % 10007)
    return

S11726()