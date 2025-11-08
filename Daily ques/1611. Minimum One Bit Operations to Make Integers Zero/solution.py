class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = 0
        toggle = 0
        while n:
            toggle ^= n
            res = toggle
            n >>= 1
        return res
