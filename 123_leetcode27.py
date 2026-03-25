class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        count = 0

        for j in range(len(nums)):
            if nums[j] == val:
                count += 1

        if count == 0:
            return len(nums)

        for i in range(count):
            for k in range(len(nums)):
                if nums[k] == val:
                    nums.remove(nums[k])
                    break
        return len(nums)
sol = Solution()
print(sol.removeElement([3, 2], 3))

