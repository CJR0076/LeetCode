class Solution:
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result

print(Solution().subsets([1,2,3]))   
