class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l < 2:
            return 0
        profit = 0
        cmin = 0
        i = 1
        while i < l:
            if prices[i] < prices[cmin]:
                cmin = i
            newp = prices[i] - prices[cmin]
            if newp > profit:
                profit = newp
            # print(i, cmin, profit)
            i += 1
        return profit


if __name__ == "__main__":
    p = [2, 1, 2, 1, 0, 1, 2]
    #p = [3,3,5,0,0,3,1,4]
    sol = Solution()
    r = sol.maxProfit(p)
    print(r)
