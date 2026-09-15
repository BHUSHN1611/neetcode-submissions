class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.insert(i,nums[i])
            ans.insert(len(nums)+i,nums[i])
        return ans
        