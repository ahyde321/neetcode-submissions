class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0:
            return []

        word_map = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in word_map:
                word_map[key] = []
            word_map[key].append(word)
        
        return list(word_map.values())


        