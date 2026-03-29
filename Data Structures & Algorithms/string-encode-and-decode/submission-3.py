class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ''.join(f'{len(s)}#{s}' for s in strs)
        return enc

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        
        while i < (len(s)):
            j = i

            while j<len(s) and s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            word = s[i:i+length]
            res.append(word)
            i += length

        return res


