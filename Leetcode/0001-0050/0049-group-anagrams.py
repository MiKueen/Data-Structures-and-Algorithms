'''
Author : MiKueen
Level : Medium
Problem Statement : Group Anagrams

Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
All inputs will be in lowercase.
The order of your output does not matter.
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        primes= [2,   3,  5,  7,  11,  13,  17,
                19,  23,  29,  31,  37,  41,  43,
                47,  53,  59,  61,  67,  71,
                73,  79,  83,  89,  97,  101]

        def get_hash(s):
            ord_a = ord('a')
            hash = 1
            for c in s:
                hash *= primes[ ord(c) - ord_a ]
            return hash
        
        mapping, res = {}, []
        for s in strs:
            a = get_hash(s)
            if mapping.has_key(a):
                mapping[a].append(s)
            else:
                temp = [s]
                mapping[a] = temp
                res.append(temp)
        for s in res:
            s.sort()
            
        return res
        