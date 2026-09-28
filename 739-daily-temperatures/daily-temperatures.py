class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n=len(temperatures)
        answer=[0] * n
        stack=[] 
        
        for i in range(n):
            ctemp=temperatures[i]
            while stack and temperatures[stack[-1]]<ctemp:
                prev_idx=stack.pop()
                answer[prev_idx]=i-prev_idx
            stack.append(i)
            
        return answer
