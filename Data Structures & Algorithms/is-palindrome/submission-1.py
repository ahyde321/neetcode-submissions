class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        alnum_s = "".join(char for char in s if char.isalnum()).lower()

        if alnum_s[::-1] == alnum_s:
            return True
        else:
            return False



        