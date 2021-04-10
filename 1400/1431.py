# 1431. Kids With the Greatest Number of Candies 
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        maxCand = max(candies)
        for i in candies:
            output.append(i+extraCandies>=maxCand)
        return output