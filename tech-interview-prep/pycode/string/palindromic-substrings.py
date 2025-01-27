class Solution(object):
    # Let N be the length of the string. The middle of the palindrome could be in one of 2N - 1 positions: either at letter or between two letters.
    # For each center, let's count all the palindromes that have this center. Notice that if [a, b] is a palindromic interval (meaning S[a], S[a+1], ..., S[b] is a palindrome), then [a+1, b-1] is one too.
    # Algorithm
    # For each possible palindrome center,
    # let's expand our candidate palindrome on the interval [left, right] as long as we can.
    # The condition for expanding is left >= 0 and right < N and S[left] == S[right].
    # That means we want to count a new palindrome S[left], S[left+1], ..., S[right].
    def countSubstrings(self, S):
        N = len(S)
        ans = 0
        for center in range(2 * N - 1):
            left = center / 2
            right = left + center % 2
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1
        return ans