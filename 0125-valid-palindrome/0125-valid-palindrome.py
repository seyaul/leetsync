class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = []
        f = "".join(char for char in s if char.isalnum())
        f = f.lower()
        f = list(f)
        return f == f[::-1]