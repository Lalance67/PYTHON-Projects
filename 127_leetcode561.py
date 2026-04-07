class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        l = []
        l2 = []
        for i in range(len(nums)):
            if i % 2 == 0:
                l.append(nums[i])
            else:
                l.append(nums[i])
                l2.append(l)
                l = []
            
        l3 = [min(i) for i in l2]
        sum = 0
        for i in l3:
            sum += i

        return sum
sol = Solution()
print(sol.arrayPairSum([6,2,6,5,1,2]))
    
# better approach
        # return sum(sorted(nums)[::2])