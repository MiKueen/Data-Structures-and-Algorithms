'''
Author : MiKueen
Level : Medium
Problem Statement : Partition Labels

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 
Note:
S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
'''

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if len(S) == 1:
            return [1]
        
        # Time Complexity - O(n)
        # Space Complexity - O(n)
        mapping = {}
        
        # store latest index of characters
        for i, char in enumerate(S):
            mapping[char] = i
            
        left = right = 0
        res = []
        
        for i, char in enumerate(S):
            right = max(right, mapping[char])
            
            # this means a segment is found 
            if i == right:
                res.append(right - left + 1)
                
                # start another segment
                left = i + 1
                
        return res
        