class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        has={'}':'{',
        ')':'(',
        ']':'['}
        for i in s:
            if i in has:
                if stack and stack[-1]==has[i]:
                    stack.pop()
                else:
                    return False
                
            
            else:
                stack.append(i)
            
        return True if not stack else False

            

        