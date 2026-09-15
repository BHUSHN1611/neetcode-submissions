class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.insert(i,nums[i])
        for i in range(len(nums),len(nums)*2):
            ans.insert(i,nums[i-len(nums)])

        return ans
        