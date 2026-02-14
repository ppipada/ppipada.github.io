class Solution(object):
    # Pythonic with extended slices and zip syntax
    def rotate(self, A):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        A[:] = list(zip(*A[::-1]))

    # first transpose and then flip left-right
    def rotateManual(self, A):
        n = len(A)
        for i in range(n):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        for row in A:
            for j in range(n / 2):
                row[j], row[~j] = row[~j], row[j]