'''
Author : MiKueen
Level : Hard
Problem Statement : Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

NOTE:
Input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''

class Solution:
    
    # Time Complexity - O(n)
    # Space Complexity - O(1)
    
    def merge(self, intervals):
        res = []
        for i in intervals:
            if not res or res[-1][-1] < i[0]:
                res.append(i)
            else:
                res[-1][-1] = max(res[-1][-1], i[-1])      
        return res
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:    
        if not intervals:
            return [newInterval]
        
        n = len(intervals)
        for i in range(n):
            if newInterval[0] > intervals[i][0]:
                if i == n-1:
                    intervals.append(newInterval)
                else:
                    continue
                    
            if newInterval[0] <= intervals[i][0]:
                if newInterval[0] == intervals[i][0] and newInterval[1] > intervals[i][1]:
                    intervals.insert(i+1, newInterval)
                else:
                    intervals.insert(i, newInterval)
                break
                
        return self.merge(intervals)
    