'''
Author : MiKueen
Level : Medium
Company : Facebook
Problem Statement : Decode Ways

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
'''

def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0

    # DP Solution
    dp = [0]*(len(s)+1) 
    dp[0] = 1 
    dp[1] = 0 if s[0] == "0" else 1 

    for i in range(2, len(s) + 1):   
        if 0 < int(s[i-1:i]) <= 9:   
            dp[i] += dp[i - 1]    
            
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i - 2]     
            
    return dp[len(s)]
    
