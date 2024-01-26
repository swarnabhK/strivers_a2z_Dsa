
#Approach 1 brute: I came up with this brute solution where we first find all the zeroes first and store their row,col values in a set
# for each row,col value we set the corresponding row to zeroes.
def set_matrix_zero(matrix):
    s = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if(matrix[row][col]==0):
                s.add((row,col))
    for coords in s:
        row,col = coords
        for i in range(row,row+1):
            for j in range(len(matrix[0])):
                matrix[i][j]= 0
        for i in range(len(matrix)):
            for j in range(col,col+1):
                matrix[i][j] = 0
          
    print(matrix)

matrix=[[1,1,1],[1,0,1],[1,1,1]]
matrix_2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_matrix_zero(matrix)
set_matrix_zero(matrix_2)

#approach2: marking -1 the column/row we need to set to 0.
# in the next pass mark all -1 as 0

def mark_row(row,matrix):
    #mark row with -1
    for col in range(len(matrix[0])):
        if(matrix[row][col]!=0):
          matrix[row][col] = -1
def mark_col(col,matrix):
    #mark col with -1
    for row in range(len(matrix)):
        if(matrix[row][col]!=0):
          matrix[row][col]= -1
        
def set_matrix_zero2(matrix):
    rows,cols = len(matrix),len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            if(matrix[row][col]==0):
                #marking -1 the column/row we need to set to 0.
                mark_row(row,matrix)
                mark_col(col,matrix)
    #marking all the -1 with 0
    for row in range(rows):
        for col in range(cols):
            if(matrix[row][col]==-1):
                matrix[row][col] = 0


matrix_3 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_matrix_zero2(matrix_3)
print(matrix_3)


#Approach 3: Optimal solution. Using a set to keep track of row, and another set to keep track of col.
# one iteration to find the row,col of each zero
# second iteration to mark the row,col: 0 if either row or col in row_set, col_set
# TC: O(2*m*n) = O(m*n)

def set_matrix_zero3(matrix):
    rows,cols = len(matrix),len(matrix[0])
    row_set,col_set = set(),set()
    for row in range(rows):
        for col in range(cols):
            if(matrix[row][col]==0):
                row_set.add(row)
                col_set.add(col)
    for row in range(rows):
        for col in range(cols):
            if(row in row_set or col in col_set):
                matrix[row][col] = 0
    print(matrix)

matrix_4 =  [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_matrix_zero3(matrix_4)