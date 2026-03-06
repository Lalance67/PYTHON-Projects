class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ischeck = 1
        zeroed = 0
        check = 0
        nozero = 1

        for i in range(0, len(s), 1):
            if len(s) == 1:
                return True
            
            if s[i] == '0':
                nozero = 0

            if s[i] == '1':
                ischeck = 1
            else: 
                zeroed = 1
                ischeck = 0

            if zeroed and ischeck: break

        if zeroed and not ischeck:
            check = 1
        if nozero:
            check = 1

        if check:
            return True
        else: return False

