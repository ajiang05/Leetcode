class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        This is a nxn matrix so it is square
        We can do this we change 

        We can transpose the matrix and to do that we switch between the diagnol
        We can have a double for loop
        
        1: We change (1,0) and (0,1)
        2: We change (2,0) and (0,2)
        3: We change (3,0) and (0,3) and 
        """
        n = len(matrix)

        for i in range(n):
            idx = i+1
        
            while idx<n:
                matrix[i][idx], matrix[idx][i] =   matrix[idx][i],matrix[i][idx]
                idx+=1

        
        print(matrix)
                
        for i in range(n):
            matrix[i].reverse()
        
        return matrix



        