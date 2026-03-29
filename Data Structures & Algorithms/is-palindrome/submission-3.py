class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_str = ''

        # Build alnum string
        for char in s:
            if char.isalnum():
                new_str += char.lower()

        return new_str[::-1] == new_str        