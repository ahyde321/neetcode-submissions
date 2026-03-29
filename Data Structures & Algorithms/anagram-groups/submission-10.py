class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        count_map = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1
            count_map[tuple(count)].append(s)
        
        for v in count_map.values():
            res.append(v)
        
        return res


