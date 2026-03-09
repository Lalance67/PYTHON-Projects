class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str = strs[0]
        res = []
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                if strs[i][j] == str[j]:
                    res.append(str[j])
        res2 = ' '.join(res)
        return res2
sol = Solution()
pr = sol.longestCommonPrefix(["flower", "flow", "flight"])
print(pr)
