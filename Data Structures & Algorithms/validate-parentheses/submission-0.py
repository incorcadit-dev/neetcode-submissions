class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)

        for i in range(0, n):
            if(s[i] == "[" or s[i] == "{" or s[i] == "("):
                stack.append(s[i])
            elif(s[i] == "}" or s[i] == "]" or s[i] == ")"):
                if not stack: return False
                top = stack.pop()
                if (s[i] == ")" and top != "(") or (s[i] == "]" and top != "[") or (s[i] == "}" and top != "{"):
                    return False

        return(True if len(stack) == 0 else False)