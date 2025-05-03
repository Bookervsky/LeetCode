class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return '0'
        s = []
        result = []
        while n != 0:
            s.append(str(n % 2))
            n = -(n // 2)
        while s:
            result.append(s.pop())
        result = ''.join(result)
        return result