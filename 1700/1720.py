# 1720. Decode XORed Array
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        returnArray = [first]
        for i in encoded:
            first = first^i
            returnArray.append(first)
        return returnArray