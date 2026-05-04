class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums[::2]) - sum(nums[1::2])
sol = Solution()
print(sol.alternatingSum([1,3,5,7]))