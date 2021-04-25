# 1486. XOR Operation in an Array
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        returnValue = 0
        for i in range(n):
            returnValue = returnValue^(start + 2*i)
        return returnValue