class Solution(object):
    # Use inbuilt functions
    def hammingWeightBuiltin(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

    # Using bit operation to cancel a 1 in each round
    # Think of a number in binary `n = XXXXXX1000, n - 1 is XXXXXX0111`.
    # `n & (n - 1)` will be `XXXXXX0000` which just canceled the last `1`
    def hammingWeightBitwise(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c