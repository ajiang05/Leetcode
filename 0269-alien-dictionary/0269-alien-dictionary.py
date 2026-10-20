class Solution:
    def alienOrder(self, words: list[str]) -> str:
        """
        We build the topological sort first then check if there are any cycles

        We create a dictonary where letter goes to next letter

        Case 1:
            There is no prev so we add all characters of word to letter
        Case 2:
            There is a match so we move on to the next
        Case 3:
            There is not a match which means that it must come after the ith letter from previous
        
        w->t->f
        w->e
        """

        letters = {
            c: set()
            for word in words
            for c in word
        }
        prev = words[0]
        for i in range(1,len(words)):
            p,c = 0,0
            curr_word = words[i]

            if len(prev)>len(curr_word) and prev.startswith(curr_word):
                return ""

            while p<len(prev) and c<len(curr_word):
                if curr_word[c]==prev[p]:
                    p+=1
                    c+=1
                else:
                    letters[prev[p]].add(curr_word[c])
                    break
                   
            
            prev = curr_word
        
        visited = set()
        result = []
        visiting = set()
        
        def dfs(c):
            if c in visiting:
                return True
            if c in visited:
                return False
            
            visiting.add(c)

            for n in letters[c]:
                if dfs(n):
                    return True
            
            result.append(c)
            visiting.remove(c)
            visited.add(c)

            return False
        
        for c in letters:
            if c not in visited:
                if dfs(c):
                    return ""
        result.reverse()
        return ''.join(result)



            

            

        
                    

                    

                    

                    

                    


                        


