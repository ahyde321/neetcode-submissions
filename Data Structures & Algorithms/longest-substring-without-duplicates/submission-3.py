class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        
        max_len = 0
        l = 0
        hash_set = set()

        for r in range(len(s)):
            
            if s[r] in hash_set:
                while s[r] in hash_set:
                    hash_set.remove(s[l])
                    l += 1

            hash_set.add(s[r])        
            max_len = max(max_len, len(hash_set))
        
        return max_len
