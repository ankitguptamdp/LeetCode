# 1614. Maximum Nesting Depth of the Parentheses
class Solution:
    def maxDepth(self, s: str) -> int:
        maxCount = 0
        stack = []
        for i in s:
            if i == '(':
                stack.append('(')
                if len(stack)>maxCount:
                    maxCount = len(stack)
            elif i == ')':
                stack.pop()
        return maxCount
                