class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        num = int(("".join(map(str, (digits))))) + 1
        l = [int(i) for i in str(num)]

        return l 
sol = Solution()
print(sol.plusOne([9, 9]))
print(sol.plusOne([1, 0, 0, 9]))