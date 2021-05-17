from random import randint


# Global variables
NUMBER_OF_MATRIXES = 10
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
        }
    }


def generate_matrixes_dict(n):
    matrixes = dict()
    rows = randint(1,9)
    cols = randint(1,9)

    for k in range(n):
        matrixes[k] = {
            'dimension': (rows,cols),
            'matrix': []
        }
        rows = cols
        cols = randint(1,9)

    return matrixes

def matrix_generate(dimension: tuple):
    m = list()
    for a in range(dimension[0]):
        row = []
        for b in range(dimension[1]):
            row.append(randint(0,9))
        m.append(row)
    return m

def print_matrix(matrix):
    for i in matrix:
        print(i)

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

def get_dimensions(matrixes: dict):
    d = list()
    for key in range(len(matrixes.keys())):
        d.append(matrixes[key]['dimension'][0])
    d.append(matrixes[key]['dimension'][1])
    return d

def matrix_multiplication_chain(s, m, diagonals, dimensions):
    """
    m[i][j] = min(m[i][k] + m[k+1][j] + d[i] * d[k+1] * d[j+1]) 
    i <= k < j
    """
    if m[0][-1] != 0:
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

    matrix_multiplication_chain(s, m, diagonals, dimensions)

def main():
    matrixes = generate_matrixes_dict(NUMBER_OF_MATRIXES)
    # matrixes = TEST_MATRIXES

    for key in matrixes.keys():
        matrixes[key]['matrix'] = matrix_generate(matrixes[key]['dimension'])

    n = len(list(matrixes.keys()))
    m = [[0 for i in range(n)] for j in range(n)]
    s = [[0 for i in range(n)] for j in range(n)]

    diagonals = get_diagonals(n)
    dimensions = get_dimensions(matrixes)

    matrix_multiplication_chain(s, m, diagonals, dimensions)
    print_matrix(s)
    print()
    print_matrix(m)

    print(f"\nMinimun cost is {m[0][-1]}")
        
if __name__ == '__main__':
    main()