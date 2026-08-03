class Solution:
    def trap(self, h: List[int]) -> int:
        if not h:
            return 0
        
        l,r=0,len(h)-1
        l_max,r_max=h[l],h[r]
        water_trapped=0

        while l<r:
            if l_max<r_max:
                l+=1
                l_max=max(l_max,h[l])
                water_trapped+=l_max-h[l]
            else:
                r-=1
                r_max=max(r_max,h[r])
                water_trapped+=r_max-h[r]
        return water_trapped
        