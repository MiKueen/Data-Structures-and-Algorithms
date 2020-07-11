'''
Author : MiKueen
Level : Medium
Problem Statement : Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 
                   6:"mno", 7:"pqrs", 8:"tuv", 9:"wzxy"}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return mapping[int(digits[0])]
        res = [""]
        for i in digits:
            temp = []
            for char in mapping[int(i)]:
                for j in res:
                    temp.append(j + char)
            res = temp
        return res
            