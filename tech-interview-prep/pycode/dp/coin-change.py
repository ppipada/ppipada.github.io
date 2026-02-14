class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Start with a dp array of size amount + 1. 
        # Use amount + 1 as the "max" value. 
        rs = [amount + 1] * (amount + 1)
        # No coin needed for amount zero
        rs[0] = 0
        # Calculate min counts needed for each target upto amount.
        for i in range(1, amount + 1):
            # Check for each available denomination
            for c in coins:
                if i >= c:
                    # Coins needed for target amount i is
                    # the min of (current calculated min number of coins)
                    # and (coins needed for i - c target amount + 1) 
                    rs[i] = min(rs[i], rs[i - c] + 1)

        if rs[amount] == amount + 1:
            # return -1 if calculated n coins is the "max" value set initially.
            return -1
        return rs[amount]


tm = [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1),
    ([], 11, -1),
]

if __name__ == "__main__":

    sol1 = Solution()

    for idx, nin in enumerate(tm):
        resout = sol1.coinChange(nin[0], nin[1])
        print(nin, resout, resout == nin[-1])