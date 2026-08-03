class MinStack:

    def __init__(self):
        self.stack=[]
        self.stackk=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stackk:
            self.stackk.append(val)
        else:
            self.stackk.append(min(self.stackk[-1],val))
        

    def pop(self) -> None:
        self.stack.pop()
        self.stackk.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stackk[-1]

        
