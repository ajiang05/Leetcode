class Solution:
    def isValid(self, s: str) -> bool:
        """
        We use a stack here 
        We iterate through s 
            if it is {([
                We append to stack
            if it is }])
                If stakc empty:
                    return false
                else:
                    if stack.pop = dict[c]:
                        continue
        """

        pair = {'}':'{',')':'(',']':'['}
        stack = []

        for c in s:
            if c in "{[(":
                stack.append(c)
            elif c in "})]":
                if not stack:
                    return False
                elif stack.pop() != pair[c]:
                    return False
        
        return len(stack)==0

