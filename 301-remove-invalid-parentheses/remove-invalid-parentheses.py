from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string: str) -> bool:
            """function to check parenthesis string."""
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = deque([s])
        visited = {s}
        result = []
        found = False
        
        while queue:
            level_size = len(queue)
            level_solutions = []
            
            for _ in range(level_size):
                curr = queue.popleft()
                
                if is_valid(curr):
                    level_solutions.append(curr)
                    found = True
                if found:
                    continue
                for i in range(len(curr)):
                    if curr[i] not in ('(', ')'):
                        continue
                    next_state = curr[:i] + curr[i+1:]
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append(next_state)
            if found:
                return level_solutions
                
        return [""]
