# 1342. Number of Steps to Reduce a Number to Zero
class Solution:
    def countSetBits(self, n):
        count = 0
        while (n):
            n &= (n-1)
            count+= 1     
        return count
    
    def numberOfSteps(self, num: int) -> int:
        return len(bin(num)[2:])-1 + self.countSetBits(num)
