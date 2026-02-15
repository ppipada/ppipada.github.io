class Solution1(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        if n == 1:
            return 1
        f = 1
        s = 2
        for _ in range(3, n + 1):
            t = f + s
            f = s
            s = t
        return s


class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        if n == 1:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


tm = [
    (1, 1),
    (2, 2),
    (3, 3),
    (0, 0),
    (None, 0),
]

if __name__ == "__main__":

    sol1 = Solution1()
    sol2 = Solution2()

    for idx, nin in enumerate(tm):
        resout = sol1.climbStairs(nin[0])
        print(nin, resout, resout == nin[1])
        resout = sol2.climbStairs(nin[0])
        print(nin, resout, resout == nin[1])