# 1221. Split a String in Balanced Strings
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        countR = 0
        countL = 0
        for i in s:
            if i == 'R':
                countR += 1
            else:
                countL += 1
            if countR == countL:
                count += 1
                countR = 0
                countL = 0
        return count
                
        