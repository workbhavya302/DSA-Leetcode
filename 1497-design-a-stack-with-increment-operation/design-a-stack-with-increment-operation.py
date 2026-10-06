class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        # increments each index position
        self.inc = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        
        idx = len(self.stack) - 1
        # Calculate the actual value 
        actual_val = self.stack.pop() + self.inc[idx]
        
        # increment to the next element if it exists
        if idx > 0:
            self.inc[idx - 1] += self.inc[idx]
            
        # Reset the increment 
        self.inc[idx] = 0
        return actual_val

    def increment(self, k: int, val: int) -> None:
        # Determine the upper limit index to apply the increment
        idx = min(k, len(self.stack)) - 1
        if idx >= 0:
            self.inc[idx] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)