class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Initialise a empty hash_map 
        # Loop through str list
        # In each iteration, sort the str
        # If the key is new, create a new record in the
        # hash_map and add the original str to the value array
        # else find the existing key and add the original string to the value area
        # return array of map values

        if len(strs) == 0:
            return []

        key_map = {}

        for s in strs:
            key = "".join(sorted(s))
            
            if key not in key_map:
                key_map[key] = []
            key_map[key].append(s)

        
        return list(key_map.values())
        

