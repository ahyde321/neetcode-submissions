class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ''.join(f'{len(s)}#{s}' for s in strs)
        print(enc)
        return enc

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            
            word = s[i:i+length]
            output.append(word)
            
            i += length
        return output