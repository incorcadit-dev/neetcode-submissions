class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for item in s:
            if item in brackets.keys():
                if stack and stack[-1] == brackets[item]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(item)

               

        return len(stack) == 0 

        