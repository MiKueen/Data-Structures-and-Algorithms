'''
Author : MiKueen
Level : Medium
Problem Statement : Rotting Oranges

In a given grid, each cell can have one of three values:
the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

Note:
1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        if rows == 0:  
            return -1
       
        fresh, rotten = 0, deque()
        time = 0
    
        # traverse grid
        for r in range(rows):
            for c in range(cols):
                
                # append co-ordinates of rotten oranges to queue
                if grid[r][c] == 2:
                    rotten.append((r, c))
                    
                # keep count of fresh oranges
                elif grid[r][c] == 1:
                    fresh += 1
                    
        # Using BFS
        # traverse grid untill the queue is not empty and there are still fresh oranges left
        while rotten and fresh:
            time += 1
            
            for ele in range(len(rotten)):
                x, y = rotten.popleft()
                
                # to check all 4 adjacent positions of rotten orange
                for i, j in [(1,0), (-1,0), (0,1), (0,-1)]:
                    adj_x, adj_y = x + i, y + j
                    
                    # continue if you go beyond boundary of grid
                    if adj_x < 0 or adj_x == rows or adj_y < 0 or adj_y == cols:
                        continue
                        
                    # change neighbouring fresh oranges to rotten oranges and append to queue
                    if grid[adj_x][adj_y] == 1:
                        grid[adj_x][adj_y] = 2
                        rotten.append((adj_x, adj_y))
                        fresh -= 1
                
        if fresh == 0:
            return time
        else:
            return -1
        