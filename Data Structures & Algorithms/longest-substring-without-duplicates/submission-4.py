class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # loop through
        # track prev unique index with lagging character
        # while loop that if invalid char is found then the pointer ..
        # .. loops until all chars in str are unique
        
        chars = []
        res = 0

        for c in s:
            if c in chars:
                while c in chars:
                    chars.pop(0)
            chars.append(c)
            res = max(res, len(chars))
            
        return res