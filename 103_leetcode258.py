class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        def add(num):
            sum = 0
            while num > 0:
                sum += (num % 10)
                num //= 10
            return sum

        while 1:            
            if num < 10:
                return num
            else: num = add(num)

sol = Solution()
print(sol.addDigits(101))



