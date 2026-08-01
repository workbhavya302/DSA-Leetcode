class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        hashmap={}
        for i,num in enumerate(n):
            complement=target-num

            if complement in hashmap:
                return [hashmap[complement],i]

            hashmap[num]=i
        