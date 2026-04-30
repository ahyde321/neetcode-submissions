class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_count = {}
        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1

        for l in range(len(s2)):
            s2_count = {}
            r = l
            
            while r < len(s2) and s2[r] in s1:
                s2_count[s2[r]] = s2_count.get(s2[r], 0) + 1
                if s2_count[s2[r]] > s1_count[s2[r]]:
                    break
                elif s1_count == s2_count:
                    return True
                r += 1
        
        return False

        