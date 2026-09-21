class Solution:
    def frequencySort(self, s: str) -> str:
        counts={}
        for char in s:
            counts[char]=counts.get(char,0)+1
        buckets=[[] for _ in range(len(s)+1)]
        for char,freq in counts.items():
            buckets[freq].append(char)
        result=[]
        for freq in range(len(buckets)-1,0,-1):
            for char in buckets[freq]:
                result.append(char*freq)
                
        return "".join(result)
