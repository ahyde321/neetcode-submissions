class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hash_set = set()
        max_len = 0

        l = 0
        for r in range(len(s)):

            if s[r] in hash_set:
                while s[r] in hash_set:
                    hash_set.remove(s[l])
                    l += 1

            hash_set.add(s[r])
            max_len = max(max_len, len(hash_set))

        return max_len


