class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        We can just create an 2-d array with numRows
        We append to each one ad once we reach ind we go again
        """
        if numRows==1:
            return s

        result = [""]*numRows
        print(result)
        j = 0
        add = 0

        for i in range(len(s)):
            if j==0:
                add = 1
            if j==len(result)-1:
                add = -1
            
            result[j]+=s[i]
            j+=add
        
        return ''.join(result)
        
        

                