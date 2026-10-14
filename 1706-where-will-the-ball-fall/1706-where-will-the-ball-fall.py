class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        """
        Cases where ball can move:
            if grid[i] == grid[grid[i]+i]
        Cases where ball cannot move anywhere:
            if grid[grid[i]+i] out of range:
            
            if grid[i] != grid[grid[i]+i]

        We can process all balls as we go down
        balls = [i for i in range(len(grid[0]))]

        for r in range(ROW):
            for b in range(len(balls)):
                val = grid[r][b]
                if balls[b]==-1:
                    continue
                if b+val<0 or b+val>=ROW:
                    balls[b] = -1
                    continue
                if grid[r][b+val]!=grid[r][b]:
                    balls[b] = -1
                    continue
                
                balls[b] = b+val     
        """

        """
        [1,2,2,3,4]
        """
        balls = [i for i in range(len(grid[0]))]
        COL = len(grid[0])
        ROW = len(grid)
        for r in range(ROW):
            for b in range(len(balls)):

                index_ball = balls[b]
                val = grid[r][index_ball]

                if index_ball==-1:
                    continue
                if index_ball+val<0 or index_ball+val>=COL:
                    balls[b] = -1
                    continue
                if grid[r][balls[b]+val]!=grid[r][balls[b]]:
                    balls[b] = -1
                    continue
                
                balls[b] = index_ball+val 
        

        
        return balls