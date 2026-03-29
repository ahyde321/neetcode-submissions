class MinStack:

    def __init__(self):
        self.stack = []
        self.min_track = []
        self.min_val = None

    def push(self, val: int) -> None:
        if self.min_val is None:
            self.min_val = val
        elif val < self.min_val:
            self.min_val = val
        self.min_track.append(self.min_val)
        self.stack.append(val)
        return None
        

    def pop(self) -> None:

        self.stack.pop()
        self.min_track.pop()

        if len(self.min_track) > 0:
            self.min_val = self.min_track[-1]
        else:
            self.min_val = None
        
        return None
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_track[-1]
        
