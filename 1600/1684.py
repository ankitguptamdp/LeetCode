# 1684. Count the Number of Consistent Strings
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for i in words:
            for j in allowed:
                i = i.replace(j,'')
            if i == '':
                count += 1
        return count