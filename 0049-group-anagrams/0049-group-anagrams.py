class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        For each word we create a dict
        We check if that that dict is equal to any other dict

        We can make a key a array for [0]*26
        Then we count the frequency and see if there is already an array like that
        if it is we add to it then we just get all thes values and return
        """
        freq = {}
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            count = tuple(count)

            if count in freq:
                freq[count].append(word)
            else:
                freq[count] = [word]
        
        
        return list(freq.values())


        