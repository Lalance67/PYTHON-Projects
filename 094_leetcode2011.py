class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        return (operations.count("X++") + operations.count("++X")) \
        - (operations.count("X--") + operations.count("--X"))
sol = Solution()
print(sol.finalValueAfterOperations(["++X", "--X", "X++"]))

