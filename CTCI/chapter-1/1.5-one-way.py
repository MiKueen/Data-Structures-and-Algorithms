'''
Author : MiKueen
Problem Statement : One Way

There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.

EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false 
'''

def one_way(word1, word2):
    if abs(len(word1) - len(word2)) > 1:
        return False

    # DP Solution
    m = len(word1)
    n = len(word2)
    dp = [[0] * (n + 1) for i in range(m + 1)]

    for j in range(n + 1):
        dp[0][j] = j
    for i in range(m + 1):
        dp[i][0] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    if dp[m][n] <= 1:
        return True
    else:
        return False