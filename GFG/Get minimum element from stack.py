class stack:
    def __init__(self):
        self.s = []
        self.minEle = None

    def push(self, x):
        self.minEle = x if not self.minEle else min(self.minEle, x)
        self.s.append((x, self.minEle))

    def pop(self):
        if not self.s:
            return -1

        elm, _ = self.s.pop()
        if self.minEle == elm:
            if self.s:
                self.minEle = self.s[-1][1]
            else:
                self.minEle = None
        return elm

    def getMin(self):
        if not self.s:
            return -1
        return self.minEle
