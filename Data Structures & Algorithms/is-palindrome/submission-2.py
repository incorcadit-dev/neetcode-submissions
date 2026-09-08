class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join(char.lower() for char in s if char.isalnum())
        l = 0
        r = len(text) - 1

        while l < r:
            if text[l] != text[r]:
                return False
            l += 1
            r -= 1

        return True