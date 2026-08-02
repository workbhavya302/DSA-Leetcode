class Solution:
    def threeSum(self, num: list[int]) -> list[list[int]]:
        num.sort()
        res=[]

        for i in range(len(num)-2):
            if i>0 and num[i]==num[i-1]:
                continue
            if num[i]>0:
                break

            l,r=i+1,len(num)-1
            while l<r:
                s=num[i]+num[l]+num[r]
                if s>0:
                    r-=1
                elif s<0:
                    l+=1
                else:
                    res.append([num[i],num[l],num[r]])
                    l+=1
                    r-=1
                    while l<r and num[l]==num[l-1]:
                        l+=1
                    while l<r and num[r]==num[r+1]:
                        r-=1
        return res            


        