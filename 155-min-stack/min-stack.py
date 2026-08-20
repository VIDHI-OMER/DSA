class MinStack:

    def __init__(self):
        self.st=[]
        self.mini=[]
    def push(self, value: int) -> None:
        self.st.append(value)
        if self.mini:
            self.mini.append(min(value, self.mini[-1]))
        else:
            self.mini.append(value)
    def pop(self) -> None:
        self.st.pop()
        self.mini.pop()
    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.mini[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()