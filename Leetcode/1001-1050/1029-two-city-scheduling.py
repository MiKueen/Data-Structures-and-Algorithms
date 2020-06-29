'''
Author : MiKueen
Level : Easy
Problem Statement : Two City Scheduling

There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], 
and the cost of flying the i-th person to city B is costs[i][1].
Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Example 1:
Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.
The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
'''

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda c: abs(c[0]-c[1]), reverse=True)
        res = 0
        limit_a = limit_b = len(costs) / 2
        
        for a, b in costs:
            if limit_a > 0 and limit_b > 0:
                temp_min = min(a,b)
                if temp_min == a:
                    limit_a -= 1
                else:
                    limit_b -= 1
                res += temp_min
            elif limit_a == 0:
                res += b
            else:
                res += a
                
        return res
    