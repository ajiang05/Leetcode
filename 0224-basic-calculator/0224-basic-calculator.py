class Solution:
    def calculate(self, s: str) -> int:
        """
        We can use a stack for the parentheses
        We just iterate through s
        We can remove whitespace

        For the stack we append parentheses and once we hit a closing one we are done 

        Once we hit closing we can start popping until we hit a opening

        We can have a array that keeps nums 

        If not we opertion
        """
        stack = []
        result = 0
        number = 0
        sign = 1

        for c in s:
            if c.isdigit():
                number = 10*number+int(c)
            if c=='(':
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1
            elif c==')':
                result+=(sign*number)
                number = 0
                
                curr_sign = stack.pop()
                prev_result = stack.pop()

                result = prev_result+(curr_sign*result)
                
            elif c=='+':
                result+=(sign*number)
                number = 0
                sign = 1
            elif c=='-':
                result+=(sign*number)
                number = 0
                sign = -1
        
        result+=(sign*number)
    
        return result

        
            


