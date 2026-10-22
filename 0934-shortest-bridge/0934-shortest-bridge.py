
from collections import deque
class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        """
        We are trying to connect two islands

        I can thinking of doing bfs to find all the nodes of one islands. Then I want to add all edges of that islands so that is if we go any four direction and a zero we add it to an edges array

        Then I can from thos edges I can perform dfs in every direction to see if I can find the next island. I would need to compare against a seen though so that a one we see is not our own island

        we append queue

        We check all four directions and check if it is one if it is we mark -1
        """
        
        n = len(grid)
        break_outer = False
        seen = set()
        edges = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c]==1:
                    queue = deque()
                    queue.append((r,c))
                    grid[r][c] = -1

                    while queue:
                        popped = queue.popleft()

                        r1,c1 = popped[0],popped[1]

                        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                            nr,nc = r1+dr,c1+dc
                            if nr>=0 and nr<n and nc>=0 and nc<n and (nr,nc) not in seen:
                                seen.add((nr,nc))
                                if grid[nr][nc]==1:
                                    grid[nr][nc]==-1
                                    queue.append((nr,nc))
                                else:
                                    edges.append((nr,nc))
                    break_outer = True
                    break
            if break_outer:
                break

        distance = 1
        while edges:
            for i in range(len(edges)):
                popped = edges.popleft()

                r1,c1 = popped[0],popped[1]

                for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr,nc = r1+dr,c1+dc

                    if nr>=0 and nr<n and nc>=0 and nc<n and (nr,nc) not in seen:
                        seen.add((nr,nc))
                        if grid[nr][nc]==1:
                            return distance
                        if grid[nr][nc]==0:
                            edges.append((nr,nc))
            distance+=1