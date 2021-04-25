# 1313. Decompress Run-Length Encoded List
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        returnArray = []
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i+1]
            for j in range(freq):
                returnArray.append(val)
        return returnArray