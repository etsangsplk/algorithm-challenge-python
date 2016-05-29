class Solution(object):
    """
    Given an integer matrix, find the length of the longest increasing path.
    From each cell, you can either move to four directions: left, right, up or
    down.
    You may NOT move diagonally or move outside of the boundary (i.e.
    wrap-around is not allowed).
    """

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        maxPath = 0
        # The boundary.
        if matrix:
            lenRow = len(matrix)
            lenCol = len(matrix[0])
            # Create a copy of the given matrix, where the elements are -1.
            visitedPath = [[0] * len(matrix[0]) for _ in range(len(matrix))]
            # Do DFS (or BFS, A*, ...whatever) to every element in the matrix.
            for row in range(lenRow):
                for col in range(lenCol):
                    maxPath = max(maxPath, self.doDFS(matrix,
                                                      lenRow - 1,
                                                      lenCol - 1,
                                                      None,
                                                      (row, col),
                                                      visitedPath))
            return maxPath
        else:
            return 0

    def doDFS(self, mat, maxRow, maxCol, prevPath, currPath, visitedPath):
        """
        :param mat: List[List[int]]
        :param prevPath: (row, col) tuple
        :param currPath: (row, col) tuple
        :param visitedPath: List[List[int]], the memorization matrix.
        longest increasing path as the value.
        :return: int, the longest increasing path.
        """
        # The current traversing row and col.
        currRow = currPath[0]
        currCol = currPath[1]

        if prevPath:
            prevRow = prevPath[0]
            prevCol = prevPath[1]
            if mat[prevRow][prevCol] >= mat[currRow][currCol]:
                # Stop when the value of current node isn't greater than the
                # previous one.
                return 0
        if visitedPath[currRow][currCol]:
            return visitedPath[currRow][currCol]

        # Keep going forward through the paths #################################
        # Look right.
        nextPath = (currRow, min(currCol + 1, maxCol))
        pathR = self.doDFS(mat, maxRow, maxCol, currPath, nextPath, visitedPath)
        # Look down.
        nextPath = (min(currRow + 1, maxRow), currCol)
        pathD = self.doDFS(mat, maxRow, maxCol, currPath, nextPath, visitedPath)
        # Look left.
        nextPath = (currRow, max(currCol - 1, 0))
        pathL = self.doDFS(mat, maxRow, maxCol, currPath, nextPath, visitedPath)
        # Look up.
        nextPath = (max(currRow - 1, 0), currCol)
        pathU = self.doDFS(mat, maxRow, maxCol, currPath, nextPath, visitedPath)

        # Going backward to the visited paths ##################################
        maxPath = max(max(pathR, pathD), max(pathL, pathU))
        if maxPath:
            visitedPath[currRow][currCol] = maxPath + 1
        else:
            visitedPath[currRow][currCol] = 1
        return visitedPath[currRow][currCol]


if __name__ == "__main__":
    sol = Solution()
    print "Given [[9,9,4],\n" \
          "       [6,6,8],\n" \
          "       [2,1,1]]\n," \
          "the answer is %d and expected answer is 4" % \
          sol.longestIncreasingPath([[9, 9, 4],
                                     [6, 6, 8],
                                     [2, 1, 1]])
    print "Given [[7,7,5],\n" \
          "       [2,4,6],\n" \
          "       [8,2,0]],\n" \
          "the answer is %d and expected answer is 4" % \
          sol.longestIncreasingPath([[7, 7, 5],
                                     [2, 4, 6],
                                     [8, 2, 0]])
    print "Given [[7,8,9],\n" \
          "       [9,7,6],\n" \
          "       [7,2,3]],\n" \
          "the answer is %d and expected answer is 6" % \
          sol.longestIncreasingPath([[7, 8, 9],
                                     [9, 7, 6],
                                     [7, 2, 3]])
    print "Given [...super big matrix...],\n" \
          "the answer is %d and expected answer is 8" % \
          sol.longestIncreasingPath(
          [[0, 4, 9, 11, 5, 11, 14, 17, 16, 11, 7, 6, 4, 16, 0, 0, 8, 3, 9, 18,
            3, 9, 14, 10, 11, 0, 18, 1, 8, 15, 10, 11, 17, 11, 18, 10, 1, 13,
            15, 15, 11, 1, 4, 15, 15, 12, 19, 13, 5, 1, 2, 10, 1, 6, 4, 3, 6,
            17, 18, 7, 19, 3, 3, 15, 16, 18, 13, 3, 5, 11, 6, 16, 2, 2, 0, 8, 3,
            5, 11, 10, 15, 5, 16, 10, 13, 9, 8],
           [9, 10, 5, 19, 2, 14, 18, 9, 18, 9, 11, 15, 14, 18, 16, 17, 15, 0, 0,
            19, 3, 17, 11, 10, 7, 1, 2, 2, 6, 11, 13, 7, 15, 3, 2, 1, 19, 16,
            11, 10, 6, 1, 8, 10, 16, 15, 4, 1, 5, 17, 10, 5, 2, 13, 9, 10, 8,
            19, 7, 5, 2, 0, 3, 1, 10, 5, 2, 17, 5, 14, 7, 2, 12, 14, 8, 17, 8,
            13, 16, 14, 11, 10, 8, 16, 1, 10, 3],
           [9, 12, 5, 10, 0, 15, 4, 2, 14, 2, 1, 7, 19, 1, 16, 9, 3, 16, 18, 2,
            9, 7, 8, 0, 0, 11, 9, 18, 9, 2, 13, 10, 9, 9, 19, 5, 11, 4, 15, 15,
            14, 7, 5, 7, 1, 13, 9, 14, 0, 10, 8, 4, 9, 19, 19, 11, 15, 17, 16,
            9, 2, 11, 14, 18, 11, 17, 10, 18, 7, 9, 12, 9, 13, 5, 15, 8, 5, 15,
            2, 10, 13, 1, 4, 9, 2, 6, 3],
           [10, 18, 7, 17, 7, 14, 3, 12, 14, 19, 16, 17, 4, 8, 15, 0, 1, 10, 7,
            6, 0, 7, 3, 11, 19, 9, 10, 6, 16, 6, 11, 8, 4, 7, 7, 6, 9, 2, 7, 12,
            7, 9, 4, 16, 19, 8, 4, 6, 18, 7, 18, 18, 2, 6, 7, 11, 0, 10, 1, 11,
            7, 0, 19, 13, 13, 17, 10, 14, 3, 9, 9, 2, 4, 13, 7, 3, 14, 1, 7, 12,
            5, 6, 14, 3, 13, 18, 13],
           [15, 11, 10, 18, 13, 17, 17, 12, 11, 15, 15, 16, 2, 5, 7, 11, 5, 14,
            11, 18, 6, 19, 15, 5, 3, 10, 1, 11, 17, 7, 16, 8, 3, 8, 2, 1, 18,
            18, 16, 5, 6, 11, 14, 8, 16, 3, 5, 8, 10, 4, 19, 13, 9, 1, 17, 8,
            18, 16, 10, 9, 9, 15, 15, 16, 14, 12, 6, 9, 13, 6, 10, 7, 13, 16, 3,
            12, 2, 6, 2, 13, 9, 3, 16, 12, 4, 8, 15],
           [15, 19, 11, 10, 7, 1, 12, 7, 6, 17, 15, 11, 7, 18, 9, 18, 15, 9, 8,
            0, 18, 2, 4, 7, 13, 9, 2, 0, 15, 16, 4, 5, 10, 19, 1, 18, 10, 7, 8,
            17, 5, 0, 8, 7, 3, 13, 19, 0, 18, 10, 3, 18, 19, 6, 14, 11, 8, 3, 6,
            5, 9, 16, 13, 9, 9, 1, 19, 4, 2, 6, 14, 16, 17, 14, 0, 2, 9, 3, 15,
            17, 12, 7, 2, 9, 7, 13, 1],
           [3, 2, 15, 10, 9, 7, 4, 15, 16, 17, 2, 7, 17, 2, 6, 2, 13, 19, 8, 2,
            2, 0, 2, 11, 0, 11, 9, 12, 9, 5, 3, 7, 10, 12, 0, 15, 6, 5, 16, 6,
            4, 13, 2, 5, 4, 16, 11, 0, 15, 2, 1, 10, 10, 13, 16, 19, 14, 13, 0,
            10, 6, 18, 17, 17, 16, 1, 19, 12, 13, 10, 12, 10, 12, 6, 1, 0, 15,
            18, 18, 8, 15, 14, 2, 2, 18, 8, 0],
           [13, 18, 5, 7, 12, 3, 11, 1, 12, 6, 13, 15, 2, 2, 4, 5, 3, 13, 14,
            18, 13, 9, 17, 9, 6, 8, 15, 15, 7, 5, 17, 18, 14, 8, 7, 19, 13, 2,
            5, 13, 10, 7, 12, 17, 5, 5, 17, 13, 17, 6, 15, 5, 3, 1, 1, 14, 10,
            6, 6, 12, 8, 8, 0, 18, 18, 17, 12, 16, 17, 14, 15, 16, 17, 19, 19,
            9, 16, 2, 6, 10, 12, 0, 16, 12, 19, 5, 17],
           [4, 12, 14, 10, 4, 10, 4, 4, 12, 9, 16, 2, 5, 9, 2, 11, 2, 7, 3, 17,
            19, 8, 17, 19, 7, 16, 13, 6, 13, 12, 3, 6, 3, 4, 19, 3, 0, 4, 7, 18,
            4, 15, 2, 0, 7, 9, 19, 11, 19, 2, 15, 19, 10, 8, 1, 11, 0, 6, 16,
            12, 1, 11, 13, 9, 7, 2, 17, 17, 15, 16, 10, 14, 11, 4, 6, 15, 9, 4,
            14, 13, 3, 8, 13, 15, 3, 8, 12],
           [7, 5, 4, 19, 2, 19, 4, 5, 7, 1, 14, 5, 5, 3, 2, 9, 4, 0, 5, 12, 9,
            0, 3, 13, 13, 10, 15, 4, 7, 1, 5, 8, 4, 10, 3, 2, 12, 12, 9, 12, 11,
            15, 16, 11, 10, 17, 15, 4, 3, 3, 16, 1, 9, 4, 13, 1, 13, 5, 2, 5,
            18, 17, 7, 7, 15, 12, 11, 17, 15, 0, 9, 6, 16, 11, 8, 2, 16, 4, 6,
            7, 16, 8, 18, 8, 7, 5, 2],
           [14, 11, 7, 12, 2, 1, 11, 1, 15, 3, 5, 1, 5, 14, 14, 10, 3, 9, 8, 15,
            10, 16, 10, 12, 10, 0, 19, 8, 14, 19, 2, 8, 4, 12, 12, 7, 7, 18, 11,
            12, 17, 14, 3, 15, 10, 17, 7, 16, 7, 19, 14, 3, 11, 5, 16, 1, 12,
            16, 8, 4, 10, 18, 16, 4, 10, 16, 16, 14, 18, 7, 16, 7, 9, 2, 17, 14,
            10, 12, 7, 16, 9, 14, 9, 1, 2, 15, 1],
           [8, 19, 15, 4, 19, 1, 7, 18, 1, 10, 19, 19, 9, 14, 16, 18, 15, 7, 5,
            7, 3, 19, 8, 17, 14, 3, 17, 9, 5, 19, 2, 18, 2, 9, 3, 18, 18, 1, 19,
            17, 13, 3, 8, 13, 4, 16, 3, 19, 12, 15, 7, 10, 0, 13, 4, 18, 1, 19,
            17, 18, 4, 0, 19, 19, 14, 0, 9, 18, 3, 1, 16, 5, 0, 16, 1, 11, 2, 6,
            6, 17, 1, 9, 10, 16, 11, 19, 12],
           [13, 18, 3, 15, 17, 8, 16, 13, 15, 16, 2, 1, 16, 16, 6, 12, 17, 11,
            6, 8, 12, 5, 12, 0, 1, 18, 17, 16, 15, 2, 13, 17, 12, 0, 9, 8, 13,
            2, 16, 4, 3, 10, 8, 7, 0, 15, 19, 3, 15, 5, 18, 5, 7, 12, 4, 6, 2,
            8, 19, 18, 5, 7, 16, 2, 13, 16, 10, 19, 14, 11, 6, 13, 11, 9, 10,
            15, 2, 14, 1, 7, 8, 7, 2, 2, 14, 19, 13],
           [2, 5, 18, 2, 4, 0, 12, 7, 7, 4, 1, 7, 11, 8, 5, 10, 19, 15, 4, 0, 4,
            7, 11, 2, 18, 3, 1, 3, 5, 4, 2, 8, 14, 14, 9, 12, 18, 3, 3, 3, 0, 6,
            16, 18, 11, 11, 18, 3, 10, 6, 16, 2, 11, 9, 12, 17, 19, 6, 14, 5,
            19, 6, 9, 15, 2, 0, 5, 7, 3, 19, 11, 19, 6, 15, 0, 0, 4, 15, 4, 13,
            6, 12, 16, 0, 4, 10, 4],
           [7, 2, 14, 18, 0, 0, 14, 8, 14, 0, 16, 13, 16, 5, 18, 7, 8, 8, 3, 10,
            5, 18, 9, 9, 17, 4, 15, 1, 6, 2, 13, 10, 7, 4, 2, 15, 16, 0, 10, 15,
            0, 10, 14, 10, 4, 14, 17, 5, 16, 18, 13, 17, 12, 4, 12, 12, 18, 3,
            1, 10, 12, 3, 14, 4, 10, 0, 19, 2, 1, 19, 13, 2, 17, 7, 9, 7, 5, 10,
            13, 4, 6, 13, 18, 2, 15, 4, 11],
           [4, 0, 15, 10, 9, 5, 1, 13, 5, 19, 6, 17, 9, 14, 12, 3, 9, 18, 4, 2,
            12, 12, 3, 1, 4, 15, 4, 5, 16, 5, 16, 16, 11, 8, 13, 0, 6, 19, 5, 7,
            5, 14, 10, 3, 8, 13, 12, 0, 17, 6, 19, 5, 15, 17, 19, 17, 12, 1, 11,
            0, 8, 5, 9, 19, 11, 5, 8, 4, 10, 4, 15, 2, 3, 4, 1, 10, 6, 12, 7, 4,
            4, 1, 10, 1, 9, 3, 8],
           [17, 6, 8, 14, 4, 14, 5, 6, 2, 10, 4, 0, 9, 5, 9, 14, 0, 13, 8, 18,
            10, 12, 5, 0, 19, 7, 16, 8, 15, 17, 0, 4, 13, 9, 11, 18, 8, 17, 11,
            1, 6, 11, 8, 5, 5, 2, 10, 16, 4, 2, 10, 10, 10, 17, 2, 1, 14, 6, 18,
            14, 15, 16, 19, 3, 14, 1, 6, 14, 10, 13, 12, 8, 16, 14, 9, 4, 17, 1,
            3, 15, 14, 6, 3, 11, 11, 10, 0],
           [4, 0, 18, 0, 11, 4, 17, 19, 11, 19, 2, 14, 10, 7, 8, 4, 0, 3, 10, 0,
            4, 17, 11, 8, 0, 14, 17, 19, 11, 17, 10, 3, 10, 4, 1, 13, 19, 15,
            14, 18, 6, 15, 4, 6, 15, 14, 7, 11, 5, 3, 17, 9, 5, 0, 12, 5, 6, 9,
            15, 17, 1, 7, 10, 19, 15, 12, 0, 14, 6, 19, 3, 18, 9, 16, 7, 2, 7,
            12, 16, 1, 3, 4, 6, 6, 3, 7, 7],
           [2, 15, 1, 8, 13, 18, 10, 10, 16, 10, 12, 0, 13, 13, 6, 9, 16, 4, 1,
            3, 19, 1, 5, 3, 2, 13, 2, 13, 1, 19, 10, 13, 19, 5, 4, 8, 7, 0, 9,
            17, 2, 4, 10, 11, 17, 19, 17, 15, 0, 2, 3, 8, 4, 10, 13, 11, 6, 16,
            14, 14, 18, 0, 16, 9, 15, 9, 17, 3, 12, 13, 2, 3, 9, 9, 7, 14, 0, 4,
            3, 18, 10, 9, 16, 14, 10, 0, 11],
           [17, 12, 16, 14, 5, 8, 10, 10, 12, 12, 11, 0, 17, 8, 5, 7, 17, 16,
            17, 8, 6, 10, 16, 2, 14, 18, 11, 6, 1, 8, 1, 12, 4, 6, 17, 12, 18,
            3, 6, 19, 17, 12, 14, 13, 18, 6, 14, 4, 3, 9, 0, 8, 13, 15, 16, 7,
            18, 0, 9, 11, 17, 7, 16, 19, 5, 7, 3, 3, 9, 0, 11, 12, 5, 13, 16,
            16, 6, 18, 6, 10, 4, 10, 1, 3, 9, 4, 7],
           [2, 2, 4, 19, 13, 6, 6, 2, 1, 15, 18, 9, 15, 18, 2, 17, 17, 11, 9,
            19, 1, 2, 0, 4, 13, 0, 12, 2, 5, 1, 17, 10, 6, 12, 2, 16, 19, 5, 13,
            17, 14, 7, 4, 12, 4, 13, 10, 13, 18, 4, 5, 0, 5, 4, 1, 13, 17, 12,
            0, 1, 10, 8, 8, 19, 12, 9, 1, 10, 13, 8, 5, 0, 9, 5, 17, 8, 18, 6,
            19, 17, 6, 19, 13, 14, 19, 13, 17],
           [3, 1, 8, 4, 2, 11, 12, 7, 8, 19, 19, 3, 11, 12, 12, 1, 3, 7, 4, 9,
            16, 10, 9, 1, 11, 14, 1, 13, 15, 3, 13, 11, 16, 2, 15, 17, 11, 14,
            3, 18, 4, 4, 10, 6, 12, 10, 5, 9, 11, 0, 12, 8, 10, 18, 15, 1, 11,
            5, 2, 13, 1, 9, 17, 19, 4, 19, 14, 15, 6, 9, 15, 0, 8, 15, 13, 16,
            8, 9, 8, 6, 7, 19, 10, 6, 8, 0, 18],
           [14, 7, 12, 5, 13, 9, 5, 3, 10, 13, 1, 16, 10, 16, 7, 15, 9, 14, 7,
            5, 3, 1, 0, 19, 4, 7, 5, 17, 19, 3, 11, 15, 1, 9, 3, 10, 0, 19, 19,
            12, 3, 13, 4, 10, 17, 13, 12, 15, 14, 16, 18, 9, 16, 13, 7, 11, 1,
            12, 10, 11, 11, 11, 11, 18, 13, 0, 13, 10, 4, 11, 4, 17, 6, 19, 0,
            7, 14, 13, 16, 2, 14, 10, 1, 14, 19, 17, 6],
           [17, 0, 4, 1, 9, 2, 7, 1, 0, 2, 13, 12, 13, 11, 4, 19, 0, 4, 3, 4, 8,
            16, 7, 16, 18, 6, 18, 19, 15, 4, 17, 13, 7, 18, 13, 7, 9, 3, 9, 15,
            7, 9, 7, 17, 2, 7, 7, 12, 11, 12, 6, 17, 17, 10, 9, 18, 6, 5, 14,
            18, 9, 15, 16, 1, 11, 13, 3, 4, 7, 12, 3, 19, 0, 17, 2, 19, 14, 2,
            16, 7, 8, 11, 7, 6, 13, 14, 9],
           [0, 6, 3, 9, 11, 12, 15, 19, 8, 15, 4, 16, 19, 10, 19, 6, 8, 16, 15,
            2, 8, 12, 17, 11, 0, 1, 8, 10, 12, 0, 6, 15, 17, 14, 17, 12, 17, 3,
            6, 19, 16, 9, 12, 6, 9, 11, 13, 6, 13, 9, 10, 3, 4, 9, 12, 7, 7, 12,
            12, 0, 3, 7, 19, 17, 9, 18, 2, 5, 13, 14, 11, 17, 16, 11, 12, 8, 5,
            13, 18, 18, 1, 13, 2, 2, 17, 16, 15],
           [14, 17, 15, 1, 12, 18, 9, 17, 9, 12, 2, 11, 6, 11, 6, 1, 12, 12, 15,
            1, 3, 13, 5, 10, 3, 9, 6, 0, 10, 5, 2, 2, 2, 8, 12, 18, 18, 2, 15,
            16, 8, 6, 6, 19, 3, 10, 15, 17, 19, 12, 8, 14, 9, 14, 2, 17, 9, 14,
            10, 11, 4, 5, 14, 5, 11, 18, 5, 13, 10, 7, 1, 12, 10, 15, 18, 11,
            10, 7, 4, 8, 1, 4, 17, 8, 4, 3, 9],
           [19, 4, 9, 11, 16, 6, 4, 13, 12, 15, 14, 5, 18, 13, 9, 18, 13, 19, 0,
            10, 9, 5, 10, 9, 16, 11, 9, 16, 5, 0, 18, 17, 8, 4, 0, 3, 6, 2, 3,
            14, 19, 9, 12, 4, 1, 18, 15, 7, 3, 2, 4, 2, 4, 19, 10, 4, 10, 1, 18,
            4, 12, 7, 8, 3, 8, 16, 1, 0, 9, 8, 14, 2, 13, 16, 16, 17, 19, 13,
            17, 15, 17, 5, 11, 18, 9, 5, 4],
           [6, 18, 14, 14, 17, 10, 15, 17, 19, 6, 1, 7, 4, 6, 10, 16, 1, 16, 13,
            19, 18, 15, 18, 13, 19, 17, 6, 9, 18, 2, 13, 4, 1, 0, 4, 3, 18, 17,
            7, 0, 12, 8, 11, 10, 2, 16, 18, 14, 9, 10, 15, 19, 14, 18, 6, 17,
            18, 9, 10, 2, 6, 15, 1, 17, 9, 4, 17, 17, 1, 9, 3, 10, 14, 0, 18,
            19, 13, 0, 19, 19, 13, 0, 16, 6, 5, 3, 0],
           [9, 5, 15, 8, 19, 3, 7, 16, 0, 1, 13, 6, 6, 9, 17, 4, 14, 14, 16, 1,
            8, 15, 1, 17, 9, 19, 10, 10, 3, 19, 15, 0, 19, 19, 5, 18, 6, 7, 18,
            15, 0, 18, 9, 14, 11, 18, 17, 1, 17, 12, 18, 6, 3, 19, 16, 5, 10,
            12, 4, 18, 2, 19, 9, 19, 5, 17, 12, 6, 9, 11, 5, 13, 15, 8, 15, 11,
            1, 16, 6, 10, 3, 3, 3, 19, 15, 1, 16],
           [2, 14, 15, 6, 0, 19, 3, 17, 0, 3, 14, 16, 5, 3, 12, 7, 14, 11, 13,
            2, 19, 15, 19, 15, 12, 7, 3, 11, 8, 12, 9, 1, 12, 18, 12, 0, 12, 11,
            6, 16, 7, 10, 7, 13, 6, 8, 8, 4, 2, 4, 4, 7, 11, 9, 19, 8, 18, 11,
            5, 18, 11, 10, 18, 8, 12, 10, 4, 2, 17, 16, 4, 13, 8, 10, 7, 11, 3,
            0, 16, 17, 14, 15, 11, 11, 3, 15, 4],
           [14, 4, 12, 5, 16, 7, 9, 18, 4, 9, 2, 3, 12, 9, 4, 9, 9, 12, 19, 3,
            2, 14, 3, 5, 14, 13, 8, 10, 4, 15, 9, 10, 12, 2, 5, 2, 0, 11, 17,
            16, 5, 19, 9, 12, 13, 10, 18, 17, 7, 14, 4, 19, 14, 16, 6, 9, 9, 11,
            11, 14, 15, 6, 0, 13, 7, 9, 4, 5, 4, 4, 19, 16, 12, 14, 4, 4, 3, 16,
            18, 5, 7, 6, 18, 10, 14, 9, 19],
           [10, 4, 8, 15, 11, 0, 5, 18, 13, 2, 12, 14, 5, 19, 9, 18, 14, 5, 19,
            11, 18, 12, 5, 16, 3, 14, 1, 9, 4, 0, 5, 4, 14, 15, 5, 9, 0, 3, 12,
            1, 18, 2, 11, 18, 7, 16, 8, 5, 2, 2, 9, 17, 19, 14, 15, 12, 8, 3, 6,
            8, 10, 2, 11, 4, 3, 9, 1, 8, 13, 19, 19, 16, 0, 2, 18, 17, 18, 9,
            19, 7, 16, 1, 4, 11, 18, 3, 19],
           [10, 8, 15, 5, 16, 8, 2, 12, 7, 3, 18, 9, 2, 15, 10, 13, 11, 11, 6,
            18, 7, 11, 12, 7, 5, 4, 2, 12, 4, 16, 16, 17, 11, 19, 5, 6, 8, 9,
            10, 8, 5, 8, 3, 11, 0, 2, 19, 12, 2, 0, 11, 6, 3, 18, 14, 12, 4, 14,
            4, 2, 5, 17, 13, 17, 2, 17, 17, 10, 14, 2, 19, 15, 3, 12, 3, 9, 9,
            13, 5, 18, 1, 9, 0, 11, 2, 18, 19],
           [18, 13, 11, 3, 13, 14, 4, 2, 6, 19, 19, 4, 8, 7, 6, 9, 17, 4, 13, 7,
            18, 11, 13, 2, 8, 13, 11, 17, 3, 16, 19, 3, 4, 18, 13, 12, 13, 6, 1,
            7, 2, 6, 19, 1, 0, 10, 14, 16, 5, 19, 2, 18, 15, 15, 5, 0, 13, 0, 7,
            19, 16, 8, 2, 18, 16, 1, 17, 14, 3, 11, 13, 12, 3, 11, 6, 5, 7, 13,
            5, 16, 8, 18, 11, 12, 10, 0, 2],
           [4, 19, 8, 3, 10, 17, 7, 15, 12, 16, 5, 15, 18, 6, 2, 0, 4, 10, 6, 9,
            19, 12, 9, 12, 5, 6, 4, 3, 10, 17, 11, 7, 10, 16, 16, 0, 0, 7, 5,
            17, 5, 12, 2, 11, 11, 2, 6, 17, 5, 10, 8, 14, 0, 15, 9, 10, 10, 11,
            1, 16, 15, 0, 16, 13, 6, 13, 0, 3, 12, 1, 9, 8, 8, 14, 16, 6, 17,
            19, 17, 8, 13, 9, 12, 3, 19, 4, 10],
           [8, 1, 10, 14, 13, 12, 9, 7, 15, 16, 2, 17, 10, 15, 3, 4, 13, 7, 8,
            8, 10, 17, 18, 4, 10, 14, 13, 18, 10, 12, 4, 4, 1, 12, 4, 1, 14, 8,
            6, 7, 10, 0, 18, 13, 19, 7, 13, 2, 4, 0, 3, 8, 12, 18, 6, 6, 19, 2,
            19, 14, 13, 0, 6, 3, 6, 17, 1, 16, 7, 7, 6, 0, 18, 6, 15, 6, 0, 0,
            11, 2, 0, 13, 3, 10, 9, 1, 19],
           [16, 10, 10, 2, 4, 2, 2, 10, 14, 3, 10, 13, 18, 12, 18, 10, 12, 10,
            18, 3, 18, 15, 12, 6, 1, 6, 8, 4, 9, 3, 13, 14, 14, 12, 6, 0, 4, 15,
            6, 1, 14, 18, 8, 0, 11, 17, 16, 4, 17, 14, 3, 11, 7, 10, 14, 9, 10,
            17, 14, 17, 17, 12, 2, 14, 3, 8, 14, 7, 15, 2, 1, 13, 18, 18, 3, 9,
            3, 17, 18, 14, 0, 7, 7, 10, 12, 3, 19],
           [9, 3, 14, 19, 8, 2, 18, 17, 3, 8, 11, 14, 4, 3, 5, 2, 0, 19, 1, 19,
            1, 6, 18, 3, 4, 0, 9, 12, 6, 14, 5, 5, 5, 2, 0, 3, 3, 13, 3, 17, 1,
            9, 8, 2, 7, 14, 3, 6, 14, 9, 4, 0, 8, 13, 12, 19, 12, 18, 7, 11, 9,
            7, 15, 8, 1, 11, 12, 18, 14, 8, 13, 7, 1, 5, 4, 2, 16, 19, 11, 16,
            13, 15, 18, 6, 18, 14, 13]])