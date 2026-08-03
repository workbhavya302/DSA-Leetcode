class Solution:
    def fourSum(self, n: List[int], target: int) -> List[List[int]]:
        n.sort()
        res=[]
        num=len(n)

        for i in range(num-3):
            if i>0 and n[i]==n[i-1]:
                continue
            if n[i]+n[i+1]+n[i+2]+n[i+3]>target:
                break
            if n[i]+n[num-3]+n[num-2]+n[num-1]<target:
                continue

            for j in range(i+1,num-2):
                if j>i+1 and n[j]==n[j-1]:
                    continue
                if n[i]+n[j]+n[j+1]+n[j+2]>target:
                    break
                if n[i]+n[j]+n[num-2]+n[num-1]<target:
                    continue
                l,r=j+1,num-1
                while l<r:
                    csum=n[i]+n[j]+n[l]+n[r]
                    if csum==target:
                        res.append([n[i],n[j],n[l],n[r]])
                        l+=1
                        r-=1
                        while l<r and n[l]==n[l-1]:
                            l+=1
                        while l<r and n[r]==n[r+1]:
                            r-=1
                    elif csum<target:
                        l+=1
                    else:
                        r-=1
        return res