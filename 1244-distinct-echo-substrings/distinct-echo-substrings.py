class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        nums = [ord(c) - ord('a') + 1 for c in text]
        base = 31
        mod = 10**9 + 7
        prefix_hash = [0] * (n + 1)
        base_pow = [1] * (n + 1)
        
        for i in range(n):
            prefix_hash[i + 1] = (prefix_hash[i] * base + nums[i]) % mod
            base_pow[i + 1] = (base_pow[i] * base) % mod
            
        def get_hash(left: int, right: int) -> int:
            h = (prefix_hash[right + 1] - prefix_hash[left] * base_pow[right - left + 1]) % mod
            return (h + mod) % mod

        seen_echoes = set()
        for L in range(1, n // 2 + 1):
            for i in range(n - 2 * L + 1):
                left_hash = get_hash(i, i + L - 1)
                right_hash = get_hash(i + L, i + 2 * L - 1)
                
                if left_hash == right_hash:
                    seen_echoes.add(text[i : i + 2 * L])
                    
        return len(seen_echoes)
