'''
Author : MiKueen
Level : Easy
Problem Statement : Three Consecutive Odds

Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

Example 1:
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Example 2:
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.

Constraints:
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
'''

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 0
        while i < len(arr)-2:
            j, k = i+1, i+2
            if arr[i] % 2 != 0 and arr[j] % 2 != 0 and arr[k] % 2 != 0:
                return True
            elif arr[k] % 2 == 0:
                i += 2
            elif arr[j] % 2 == 0:
                i += 1
            elif arr[i] % 2 == 0:
                i += 1
        return False
        