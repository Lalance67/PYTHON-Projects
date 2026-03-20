class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        nums.sort()
        counter = 0

        for i in range(n):
            if i == n - 1 and nums[i] == counter:
                counter += 1
                return counter
            if nums[i] == counter:
                pass
            else: return counter
            counter += 1
