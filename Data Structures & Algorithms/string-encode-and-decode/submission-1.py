class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''.join(f"{len(s)}#{s}" for s in strs)
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i <len(s):
            j = i
            while j<len(s) and s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            i = j + 1

            word = s[i:i+length]
            strs.append(word)

            i += length
            
        return strs