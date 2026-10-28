from collections import deque
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        """
        [1,2,2],
        [1,1,0],
        [0,1,1]

        [1,0,0],
        [1,1,2],
        [2,1,1]
        """
        """
        Because 3x3 we can just use backtracking
        """

        n = len(grid)
        zero = []
        more_one = []

        for r in range(n):
            for c in range(n):
                if grid[r][c]==0:
                    zero.append((r,c))
                if grid[r][c]>1:
                    for _ in range(grid[r][c] - 1):
                        more_one.append((r,c))

        def backtrack(i):
            if i==len(zero):
                return 0

            best = float('inf')
            curr_zero = zero[i]

            for j in range(len(more_one)):
                if more_one[j]==None:
                    continue
                curr_one = more_one[j]
                r_d = abs(curr_one[0]-curr_zero[0])
                c_d = abs(curr_one[1]-curr_zero[1])

                distance = r_d+c_d
                
                more_one[j] = None
                cost = distance+backtrack(i+1)
                more_one[j] = curr_one

                best = min(best,cost)
            
            return best
        
        return backtrack(0)