"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""
# def rotate(self, matrix: List[List[int]]) -> None:
def rotate(matrix):
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])
    matrix.reverse()
    for i in range(len(matrix)):
        # print(matrix[i])
        for j in range(i):
            # print(j)
            temp=matrix[j][i]
            matrix[j][i]=matrix[i][j]
            matrix[i][j]=temp
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])


rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]])

