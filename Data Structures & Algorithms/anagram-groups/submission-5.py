class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []

        key_map = {}
        
        for s in strs:
            key = ''.join(sorted(s))
            if key not in key_map:
                key_map[key] = []
            key_map[key].append(s)
        
        return list(key_map.values())



        