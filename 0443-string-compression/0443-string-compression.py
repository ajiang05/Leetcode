class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        We can go through the array of strings and have two pointers.
        Once we hit a new letter:
            we check if the freq is greater than 1 
                Then we add on to the result for each number of the freq
        """
        freq = 0
        curr_letter = chars[0]
        l = 0
        r = 0

        while r<len(chars):
            if curr_letter==chars[r]:
                freq+=1
            else:
                chars[l] = curr_letter
                l+=1
                if freq>1:
                    for digit in str(freq):
                        chars[l] = digit
                        l+=1
                freq = 1
            curr_letter = chars[r]    
            r+=1

        chars[l] = curr_letter
        l+=1
        if freq>1:
            for digit in str(freq):
                chars[l] = digit
                l+=1
        
        chars = chars[:l]
        
        return l
        
        

            
            

            
            