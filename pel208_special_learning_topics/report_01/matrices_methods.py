
def mat_mul(mat1, mat2):
    """matrix multiplication"""
    if len(mat1[0]) == len(mat2):
        n = len(mat1)
        p = len(mat2[0])
        m = len(mat1[0])
        
        mat3 = [[0 for i in range(p)] for j in range(n)]
        
        for i in range(n):
            for j in range(p):
                sum = 0
                for k in range(m):
                    sum = sum + mat1[i][k] * mat2[k][j]
                mat3[i][j] = sum
        return mat3
    
    else:
        print("Invalid multiplication")
        return -1

def find_determinant(mat):
    """calculate determinant"""
    if len(mat) == 2:
        return (mat[0][0]*mat[1][1]) - (mat[0][1]*mat[1][0])
    elif len(mat) == 3:
        
        return ((mat[0][0]*mat[1][1]*mat[2][2]) 
              + (mat[0][1]*mat[1][2]*mat[2][0]) 
              + (mat[0][2]*mat[1][0]*mat[2][1]) 
              - (mat[0][2]*mat[1][1]*mat[2][0])
              - (mat[0][1]*mat[1][0]*mat[2][2])
              - (mat[0][0]*mat[1][2]*mat[2][1])
             )
    else:
        print("Not possible to calculate")
        return -1          

def transpose(mat):
    """transpose matrix"""
    n_row = len(mat)
    n_col = len(mat[0])

    new_mat = [ [0 for i in range(n_row)] for j in range(n_col) ]

    for i in range(n_row):
        for j in range(n_col):
            new_mat[j][i] = mat[i][j]

    return new_mat

def invert_mat(mat):
    """invert matrices 2x2 and 3x3"""        
    if len(mat) == len(mat[0]):

        if len(mat) == 2:
            new_mat = [[0 for i in range(2)] for j in range(2)]
            determinant = find_determinant(mat)

            new_mat[0][0] = mat[1][1]
            new_mat[1][1] = mat[0][0] 
            new_mat[0][1] = (-mat[0][1])
            new_mat[1][0] = (-mat[1][0])

            for i in range(2):
                for j in range(2):
                    new_mat[i][j] = (1/determinant) * new_mat[i][j]
            
            return new_mat

        elif len(mat) == 3:
            new_mat = [[0 for i in range(3)] for j in range(3)]
            determinant = find_determinant(mat)

            new_mat[0][0] = +((mat[1][1] * mat[2][2]) - (mat[1][2] * mat[2][1]))
            new_mat[0][1] = -((mat[1][0] * mat[2][2]) - (mat[1][2] * mat[2][0]))
            new_mat[0][2] = +((mat[1][0] * mat[2][1]) - (mat[1][1] * mat[2][0]))
            new_mat[1][0] = -((mat[0][1] * mat[2][2]) - (mat[0][2] * mat[2][1]))
            new_mat[1][1] = +((mat[0][0] * mat[2][2]) - (mat[0][2] * mat[2][0]))
            new_mat[1][2] = -((mat[0][0] * mat[2][1]) - (mat[0][1] * mat[2][0]))
            new_mat[2][0] = +((mat[0][1] * mat[1][2]) - (mat[0][2] * mat[1][1]))
            new_mat[2][1] = -((mat[0][0] * mat[1][2]) - (mat[0][2] * mat[1][0]))
            new_mat[2][2] = +((mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0]))

            for i in range(3):
                for j in range(3):
                    new_mat[i][j] = (1/determinant) * new_mat[i][j]
            return transpose(new_mat)
        

        else:
            print("Not possible to invert")
            return -1
    else:
        print("Not possible to invert")
        return -1

def find_beta(features, target):
    """calculate beta"""
    xt_x = mat_mul(transpose(features),features)
    xt_y = mat_mul(transpose(features),target)
    beta = mat_mul(invert_mat(xt_x),xt_y)

    return beta