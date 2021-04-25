# 1389. Create Target Array in the Given Order
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        returnArray = []
        for i in range(len(nums)):
            returnArray.insert(index[i], nums[i])
        return returnArray