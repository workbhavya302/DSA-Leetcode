from collections import deque

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n=len(nums)
        prefix_sums=[0]*(n+1)
        for i in range(n):
            prefix_sums[i+1]=prefix_sums[i]+nums[i]
            
        q=deque() 
        min_len=float('inf')
        
        for i in range(n+1):
            while q and prefix_sums[i]-prefix_sums[q[0]]>=k:
                min_len=min(min_len,i-q.popleft())

            while q and prefix_sums[i]<=prefix_sums[q[-1]]:
                q.pop()
                
            q.append(i)
            
        return min_len if min_len!=float('inf') else -1

        