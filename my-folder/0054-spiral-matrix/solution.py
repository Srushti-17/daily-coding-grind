class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        top, left = 0, 0
        bottom, right = m-1, n-1
        ele = []

        while top <= bottom and left <= right:
            # left to right (top row)
            for j in range(left, right + 1):
                ele.append(matrix[top][j])
            top += 1

            # top to bottom (rightmost column)
            for i in range(top, bottom + 1):
                ele.append(matrix[i][right])
            right -= 1

            # right to left (bottom row)
            if top <= bottom:  
                for j in range(right, left - 1, -1):
                    ele.append(matrix[bottom][j])
                bottom -= 1

            # bottom to top (leftmost column)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ele.append(matrix[i][left])
                left += 1

        return ele
