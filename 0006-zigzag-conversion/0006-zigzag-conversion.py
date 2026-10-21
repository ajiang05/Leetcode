class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        We can just create an 2-d array with numRows
        We append to each one ad once we reach ind we go again
        """
        if numRows==1:
            return s

        result = [[] for i in range(numRows)]
        j = 0
        add = 0

        for i in range(len(s)):
            if j==0:
                add = 1
            if j==len(result)-1:
                add = -1
            
            result[j].append(s[i])
            j+=add
        
        print(result)
        
        result_str = ''
        for row in result:
            result_str+=''.join(row)
        
        return result_str

                