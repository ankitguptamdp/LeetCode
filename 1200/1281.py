# 1281. Subtract the Product and Sum of Digits of an Integer
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        m = copy.deepcopy(n)
        product = 1
        summation = 0
        while m:
            unit = m%10
            product = product * unit
            summation = summation + unit
            m //= 10
        return product - summation