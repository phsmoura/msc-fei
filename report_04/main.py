from pprint import pprint
from random import randint
from timeit import default_timer as timer


# Global variables
NUMBER_OF_MATRICES = 10
TEST_MATRIXES = {
        0: {
            'dimension': (3,2),
            'matrix': []
        },
        1: {
            'dimension': (2,4),
            'matrix': []
        },
        2: {
            'dimension': (4,2),
            'matrix': []
        },
        3: {
            'dimension': (2,5),
            'matrix': []
        },
        4: {
            'dimension': (5,3),
            'matrix': []
        },
        5: {
            'dimension': (3,2),
            'matrix': []
        },
        6: {
            'dimension': (2,2),
            'matrix': []
        },
        7: {
            'dimension': (2,3),
            'matrix': []
        },
        8: {
            'dimension': (3,3),
            'matrix': []
        },
        9: {
            'dimension': (3,4),
            'matrix': []
        },
    }
TIMER=[0]

def generate_matrices_dict(n):
    matrices = dict()
    rows = randint(1,9)
    cols = randint(1,9)

    for k in range(n):
        matrices[k] = {
            'dimension': (rows,cols),
            'matrix': []
        }
        rows = cols
        cols = randint(1,9)

    return matrices

def matrix_generate(dimension: tuple):
    m = list()
    for a in range(dimension[0]):
        row = []
        for b in range(dimension[1]):
            row.append(randint(0,9))
        m.append(row)
    return m

def print_matrix_latex(matrix):
    for i in matrix:
        print(str(i).replace(', ',' & ').replace('[','').replace(']','') + ' \\\\')

def get_diagonals(size: int):
    sum_ = 0
    ordered = list()

    while sum_ < size:
        for row in range(0, size):
            for col in range(row, row+1):
                if col+sum_ < size:
                    # print(row,col+sum_)
                    ordered.append((row,col+sum_))
        sum_ += 1
    return ordered[size:]

def get_dimensions(matrices: dict):
    d = list()
    for key in range(len(matrices.keys())):
        d.append(matrices[key]['dimension'][0])
    d.append(matrices[key]['dimension'][1])
    return d

def matrix_multiplication_chain(s, m, diagonals, dimensions):
    """
    m[i][j] = min(m[i][k] + m[k+1][j] + d[i] * d[k+1] * d[j+1]) 
    i <= k < j
    """
    start_timer = timer()
    if m[0][-1] != 0:
        TIMER.append(timer() - start_timer + TIMER[-1])
        return

    coord = diagonals[0]
    diagonals.pop(0)

    row = coord[0]  
    col = coord[1]

    aux = {
        'values': [],
        'k': []
    }

    for k in range(row,col):
        d = dimensions[row] * dimensions[k+1] * dimensions[col+1]
        aux['values'].append(m[row][k] + m[k+1][col] + d)
        aux['k'].append(k + 1)

    lower_value = min(aux['values'])
    s[row][col] = aux['k'][aux['values'].index(lower_value)]
    m[row][col] = lower_value

    TIMER.append(timer() - start_timer + TIMER[-1])
    matrix_multiplication_chain(s, m, diagonals, dimensions)

def write_file(matrices, min_cost):
    dim = ''
    for k in matrices:
        dim += f"{matrices[k]['dimension'][0]}x{matrices[k]['dimension'][1]} & "

    dim += str(min_cost)
    dim += ' \\\\ \n'

    with open('file.tex','a') as f:
        f.write(dim)

def write_coord_latex():
    text = ''
    for k in range(len(TIMER)):
        text += f"({k+1},{TIMER[k]}) "

    with open('coord.tex','w') as f:
        f.write(text)

def main():
    matrices = generate_matrices_dict(NUMBER_OF_MATRICES)
    # matrices = TEST_MATRIXES

    for key in matrices.keys():
        matrices[key]['matrix'] = matrix_generate(matrices[key]['dimension'])

    n = len(list(matrices.keys()))
    m = [[0 for i in range(n)] for j in range(n)]
    s = [[0 for i in range(n)] for j in range(n)]

    diagonals = get_diagonals(n)
    dimensions = get_dimensions(matrices)

    # print(f"m: {m}\ndiagonals: {diagonals}\ndimensions: {dimensions}")

    matrix_multiplication_chain(s, m, diagonals, dimensions)
    pprint(s)
    print()
    pprint(m)

    # print(f"\nMinimum cost is {m[0][-1]}")
    # write_file(matrices, m[0][-1])
    # write_coord_latex()
        
if __name__ == '__main__':
    main()