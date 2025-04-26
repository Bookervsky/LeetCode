class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(':')','[':']','{':'}'}
        for i, item in enumerate(s):
            if item in dic.keys():
                stack.append(item)
            elif stack and item == dic[stack[-1]]:
                stack.pop()
                continue
            else:
                return False
        return not stack