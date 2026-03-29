class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0:
            return []

        anagram_map = {}

        for word in strs:
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1

            key = tuple(char_count)

            if key not in anagram_map:    
                anagram_map[key] = []
            anagram_map[key].append(word)
        return list(anagram_map.values())



        