class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0: return ''
        for l in range(len(strs[0])):
            c = strs[0][l]
            for i in range(len(strs)):
                if l >= len(strs[i]) or c != strs[i][l]:
                    return strs[0][:l]
        return strs[0]


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
