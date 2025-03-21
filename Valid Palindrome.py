class Solution:
    def isPalindrome(self, s: str) -> bool:
        return (f := ''.join(c.lower() for c in s if c.isalnum())) == f[::-1]
