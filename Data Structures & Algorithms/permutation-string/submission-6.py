class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count, s2_count = {}, {}

        for i in range(len(s1)):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
        
        matches = 0
        for k, v in s1_count.items():
            if k in s2_count and s2_count[k] == v:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == len(s1_count):
                return True
            
            s2_count[s2[r]] = s2_count.get(s2[r], 0) + 1

            if s2[r] in s1_count:
                if s1_count[s2[r]] == s2_count[s2[r]]:
                    matches += 1
                elif s1_count[s2[r]] + 1 == s2_count[s2[r]]:
                    matches -= 1

            if s2[l] in s1_count:
                # if it was perfectly matched and is about to go out of alignment
                if s2_count[s2[l]] == s1_count[s2[l]]:
                    matches -= 1
                # if it was over-counted and is about to become perfectly matched
                elif s2_count[s2[l]] == s1_count[s2[l]] + 1:
                    matches += 1

            # now actually remove it from the window
            s2_count[s2[l]] -= 1
            if s2_count[s2[l]] == 0 :
                del s2_count[s2[l]]
            l += 1
        
        return matches == len(s1_count)
        




