class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_map = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            if s[r] in c_map:
                l = max(c_map[s[r]] + 1, l)
            c_map[s[r]] = r
            res = max(res, r-l + 1)
        
        return res

                


