

#Using extra space(O(m*n))
#TC: O(m*n)
def rotate_matrix(matrix):
    rows,cols = len(matrix),len(matrix[0])
    transpose =[[0] * rows for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            transpose[row][col] = matrix[cols-col-1][row]
    for row in range(rows):
        for col in range(cols):
            matrix[row][col] = transpose[row][col]


m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate_matrix(m1)
print(m1)
rotate_matrix(m2)
print(m2)

#without using extra space, we can trasnspose the matrix and reverse each row.
#TC(O(m*n))

def rotate_matrix2(matrix):
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix[0])):       
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    for row in range(len(matrix)):
        left = 0
        right = len(matrix[0])-1
        while(left<right):
            matrix[row][left],matrix[row][right] = matrix[row][right],matrix[row][left]
            left+=1
            right-=1
    
            

m3 = [[1,2,3],[4,5,6],[7,8,9]]
rotate_matrix2(m3)
print(m3)