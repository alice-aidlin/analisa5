
def main():
    points=[[0,0],[1,0.8415],[2,0.9093],[3,0.1411],[4,-0.7568],[5,-0.9589],[6,-0.2794]]
    find_point=2.5
def Linear_interpolation(points,find_point):
     for row in range(len(points) - 1):
         if find_point > points[row][0] and find_point < points[row + 1][0]:
            x1=points[row][0]
            x2=points[row+1][0]
            y1=points[row][1]
            y2=points[row+1][1]
            return (((y1 - y2) / (x1 - x2)) * find_point) + ((y2 * x1 - y1 * x2) / (x1 - x2))


def matrix_multiply(A, B):  # A function that calculates the multiplication of 2 matrices and returns the new matrix
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if colsA != rowsB:
        print('Number of A columns must equal number of B rows.')
    new_matrix = []
    while len(new_matrix) < rowsA:  # while len small the len rows
        new_matrix.append([])  # add place
        while len(new_matrix[-1]) < colsB:
            new_matrix[-1].append(0.0)  # add value
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for k in range(colsA):
                total += A[i][k] * B[k][j]  # mul mat
            new_matrix[i][j] = total
    return new_matrix  # return the A*B=new matrix
def create_I(matrix):  # A function that creates and returns the unit matrix
    I = list(range(len(matrix)))  # make it list
    for i in range(len(I)):
        I[i] = list(range(len(I)))

    for i in range(len(I)):
        for j in range(len(I[i])):
            I[i][j] = 0.0  # put the zero

    for i in range(len(I)):
        I[i][i] = 1.0  # put the pivot
    return I  # unit matrix


def inverse(matrix):  # A function that creates and returns the inverse matrix to matrix A
    new_matrix = create_I(matrix)  # Creating the unit matrix
    count = 0
    check = False  # flag
    while count <= len(matrix) and check == False:
        if matrix[count][0] != 0:  # if the val in place not 0
            check = True  # flag
        count = count + 1  # ++
    if check == False:
        print("ERROR")
    else:
        temp = matrix[count - 1]
        matrix[count - 1] = matrix[0]  # put zero
        matrix[0] = temp
        temp = new_matrix[count - 1]
        new_matrix[count - 1] = new_matrix[0]
        new_matrix[0] = temp

        for x in range(len(matrix)):
            divider = matrix[x][x]# find the div val
            if divider==0:
                divider=1
            for i in range(len(matrix)):
                matrix[x][i] = matrix[x][i] / divider  # find the new index
                new_matrix[x][i] = new_matrix[x][i] / divider
            for row in range(len(matrix)):
                if row != x:
                    divider = matrix[row][x]
                    for i in range(len(matrix)):
                        matrix[row][i] = matrix[row][i] - divider * matrix[x][i]
                        new_matrix[row][i] = new_matrix[row][i] - divider * new_matrix[x][i]
    return new_matrix  # Return of the inverse matrix


def Polynomial_interpolation(points,find_point):
    #creating a new matrix
    mat = list(range(len(points)))
    for i in range(len(mat)):
        mat[i] = list(range(len(mat)))
    for row in range(len(points)):
        mat[row][0] = 1
    for row in range(len(points)):
        for col in range(1, len(points)):
            mat[row][col] = pow(points[row][0], col)
    res_mat = list(range(len(points)))
    for i in range(len(res_mat)):
        res_mat[i] = list(range(1))
    for row in range(len(res_mat)):
        res_mat[row][0]=points[row][1]
    vector_a= matrix_multiply(inverse(mat), res_mat)
    sum = 0
    for i in range(len(vector_a)):
        if i == 0:
            sum = vector_a[i][0]
        else:
            sum +=vector_a[i][0]*find_point ** i

    print(sum)





points=[[0,0],[1,0.8415],[2,0.9093],[3,0.1411],[4,-0.7568],[5,-0.9589],[6,-0.2794]]
#points=[[1,0.8415],[2,0.9093],[3,0.1411]]
find_point=2.5
Polynomial_interpolation(points,find_point)

