# 0697. Degree of an Array
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
    
        num = nums
    
        dictionary = {}
        for i in range(len(num)):
            if num[i] not in dictionary.keys():
                dictionary[num[i]] = {
                    'count': 1,
                    'left': i,
                    'right': i
                }
            else:
                dictionary[num[i]]['count'] += 1
                dictionary[num[i]]['right'] = i

        dictionary = sorted(dictionary.items(), key = lambda kv: (-kv[1]['count'], kv[1]['right'] - kv[1]['left']))
        return dictionary[0][1]['right'] - dictionary[0][1]['left'] + 1