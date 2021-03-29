from random import randint
import matplotlib.pyplot as plt


def generate_log(message: str, array: list, overwrite: bool) -> None:
    if overwrite:
        mode = 'w'
    else:
        mode = 'a'
        
    with open ('report_02/output.log', mode) as f:
        f.write(message + '\n')
        f.write(str(array) + '\n\n')

def generate_array(size: int, max_random_number: int) -> list:
    array = list()
    i = 0
    while i < size:
        array.append(randint(0,max_random_number))
        i += 1
    return array

def create_table_latex(x: list,y: list,z: list) -> None:
    fields = '\\hline\nExecuções & Bubble(s) & Quick(s) & Randomized Quick(s)\\\\ \n\\hline'
    filename = 'report_02/table.tex'

    with open(filename,'w') as texfile:
        texfile.write(fields + '\n')
        for k in range(len(x)):
            texfile.write(f'{k+1} & {x[k]} & {y[k]} & {z[k]} \\\\\n')  

def create_coodinates_latex(name: str, meassures: list) -> None:
    filename = 'report_02/coordinates.tex'
    n = len(meassures)

    with open(filename,'a') as texfile:
        texfile.write(f'{name}:\ncoordinates {{\n')

        for k in range(n):
            texfile.write(f'({k+1},{meassures[k]})')

        texfile.write('\n};\n\n')  

def plot_graphs(x: int, y: list, name: str) -> None:
    plt.plot([*range(x)], y)
    plt.xlabel('Number of tests')
    plt.ylabel('Time (s)')
    plt.title(name)
    plt.show()