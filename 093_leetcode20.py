class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ch = 0
        l = []
        for i in s:
            if i in "[{(":
                l.append(i)
                ch += 1
            elif i in "]})":
                if not l:
                    return False
                elif i == ")" and l[len(l) - 1] == "(":
                    l.pop(len(l) - 1)
                    ch -= 1
                elif i == "}" and l[len(l) - 1] == "{":
                    l.pop(len(l) - 1)
                    ch -= 1
                elif i == "]" and l[len(l) - 1] == "[":
                    l.pop(len(l) - 1)
                    ch -= 1
                else: return False

        if ch == 0:
            return True
        else: return False
sol = Solution()
print(sol.isValid("()[]{}"))

