class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """
        We can turn digits into 
        """
        num = ""
        for d in digits:
            num+=str(d)
        int_num = int(num)
        int_num+=1

        result = []
        for d in str(int_num):
            result.append(int(d))
        
        return result
        
