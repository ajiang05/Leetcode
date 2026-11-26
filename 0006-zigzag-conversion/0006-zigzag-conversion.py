class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        We create an array of length num rows
        We append each element of s where 
            if its index 0 we +1
            if its index length-1 we -1
        We just join all the letters
        """
        if numRows==1:
            return s
        index = 0
        sign = 1
        arr = [[] for _ in range(numRows)]
        for i in range(len(s)):
            if index==0:
                sign = 1
            if index==numRows-1:
                sign = -1

            arr[index].append(s[i])
            index+=sign
        
        result = ''

        for letters in arr:
            result = result+''.join(letters)
        
        return result
        