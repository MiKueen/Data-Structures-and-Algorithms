'''
Author : MiKueen
Level : Medium
Problem Statement : Reconstruct Itinerary

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.

Example 1:
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:
Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
'''

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = {}
        for src, dest in tickets:
            if src in targets:
                targets[src].append(dest)
            else:
                targets[src] = [dest]    
        for src in targets.keys():
            targets[src].sort(reverse=True)
            
        stack, res = [], []
        stack.append("JFK")
        while len(stack) > 0:
            temp = stack[-1]
            if temp in targets and len(targets[temp]) > 0: 
                stack.append(targets[temp].pop())
            else:
                res.append(stack.pop())
        return res[::-1]
    