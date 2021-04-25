# 1528. Shuffle String
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        strArray = list(s)
        for i in range(len(indices)):
            strArray[indices[i]] = s[i]
        return ''.join(strArray)