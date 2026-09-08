class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand = ["+" , "-", "*","/"]
        stack = []

        def evaluate(firstInt, secondInt, operand):
            match(operand):
                case '+':
                    return firstInt + secondInt
                case '-':
                    return firstInt - secondInt
                case '*':
                    return firstInt * secondInt
                case '/':
                    return int(firstInt / secondInt)




        
        for item in tokens:
            if item in operand:
                secondNumber = int(stack.pop())
                firstNumber = int(stack.pop())
                stack.append(evaluate(firstNumber, secondNumber, item)) 

            else:
                stack.append(int(item))

        return stack.pop()

        