# 1470. Shuffle the Array
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list = []
        for i in range(int(len(nums)/2)):
            list.append(nums[i])
            list.append(nums[n+i])
        return list
        