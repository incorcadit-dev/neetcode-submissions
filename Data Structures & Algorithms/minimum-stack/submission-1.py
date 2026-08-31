class MinStack:

    def __init__(self):
        self._data: list = []
        self._min_stack: list = []
        

    def push(self, val: int) -> None:
        self._data.append(val)

        if (len(self._min_stack) == 0):
            self._min_stack.append(val)
        elif(len(self._min_stack) > 0):
            self._min_stack.append(min(val, self._min_stack[-1]))

        

    def pop(self) -> None:
        self._data.pop()
        self._min_stack.pop()
        

    def top(self) -> int:
        return self._data[-1]
        

    def getMin(self) -> int:
        return self._min_stack[-1]
        
