class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        
        ls = []
        
        for i in operations:
            if i == "C":
                ls.pop()
            elif i == "D":
                ls.append((ls[-1] * 2))
            elif i == "+":
                ls.append(ls[-1] + ls[-2])
            else:
                ls.append(int(i))
            
        return sum(ls)
sol = Solution()
print(sol.calPoints(["5","2","C","D","+"]))
