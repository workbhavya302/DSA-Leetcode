class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod=10**9+7
        l_add=[0]*26
        c_count=0
        for char in s:
            index=ord(char)-ord('a')
            combination=(c_count+1)%mod
            n_count=(c_count+combination-l_add[index]) % mod
            l_add[index]=combination
            c_count=n_count
        return (c_count+mod) % mod

        