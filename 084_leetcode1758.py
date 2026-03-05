class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """

        self.s = s
        count = 0
        count2 = 0

        if s[0] == '0':
            for i in range(0, len(s), 2):
                if s[i] != '0':
                    count += 1
            for j in range(1, len(s), 2):
                if s[j] != '1':
                    count += 1

            for i in range(0, len(s), 2):
                if s[i] != '1':
                    count2 += 1
            for j in range(1, len(s), 2):
                if s[j] != '0':
                    count2 += 1
        else: 
            for i in range(0, len(s), 2):
                if s[i] != '1':
                    count += 1
            for j in range(1, len(s), 2):
                if s[j] != '0':
                    count += 1
            
            for i in range(0, len(s), 2):
                if s[i] != '0':
                    count2 += 1
            for j in range(1, len(s), 2):
                if s[j] != '1':
                    count2 += 1

        return min(count, count2)
        