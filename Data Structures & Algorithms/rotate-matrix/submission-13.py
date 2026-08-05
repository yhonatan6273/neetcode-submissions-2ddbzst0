class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                

                # save the lleft
                lLeft = matrix[l][l + i]

                # move r left into l left
                matrix[l][l + i] = matrix[r - i][l]

                # move r right into r left
                matrix[r - i][l] = matrix[r][r - i]

                # move l right into r right
                matrix[r][r - i] = matrix[l + i][r]

                # move l left into l right
                matrix[l + i][r] = lLeft
            r -= 1
            l += 1