from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not s or not t:
            return ""

        window, t_count = defaultdict(int), Counter(t)
        have, need = 0, len(t_count.keys())

        res, resLen = [-1, -1], float('inf')
        l = 0
        for i in range(len(s)):

            c = s[i]
            window[c] += 1

            if c in t_count and window[c] == t_count[c]:
                have += 1

            while have == need:

                if (i - l + 1) < resLen or (i - l + 1) == resLen and s[l:i+1] < s[res[0]:res[1]]:
                    res = [l, i + 1]
                    resLen = i - l + 1
                
                leftChar = s[l]
                window[leftChar] -= 1

                if leftChar in t_count and window[leftChar] < t_count[leftChar]:
                    have -= 1
                
                l += 1
                
        return s[res[0]:res[1]]







