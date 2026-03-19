class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return not len(set(nums)) == len(nums)
sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 4, 1]))

        # n = len(nums)
        # nums.sort()
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        