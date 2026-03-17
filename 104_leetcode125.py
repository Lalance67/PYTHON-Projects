class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = [i for i in s if i.isalnum()]
        s = "".join(l).upper()
        if s == s[::-1]:
            return True
        else: return False