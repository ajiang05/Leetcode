class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        We can iterate through the whole 2d matrix and look for zero
        We then can find out which column and rows we need to fix
        r_seen = set()
        c_seen = set()

        [(0,0),(0,3)]
        """
        ROW = len(matrix)
        COL = len(matrix[0])

        zeros = []
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c]==0:
                    zeros.append((r,c))
        
        r_seen = set()
        c_seen = set()

        for r,c in zeros:
            if r not in r_seen:
                for curr_c in range(COL):
                    matrix[r][curr_c] = 0
                r_seen.add(r)
            if c not in c_seen:
                for curr_r in range(ROW):
                    matrix[curr_r][c] = 0
                c_seen.add(c)
        
        return matrix



        