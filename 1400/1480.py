# 1480. Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        list = []
        sum = 0
        for i in nums:
            sum += i
            list.append(sum)
        return list