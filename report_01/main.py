from timeit import default_timer as timer
from random import randint
from sys import maxsize
import matplotlib.pyplot as plt

measures_i = list()
measures_r = list()

def mdc_iterative(a,b,start):
    while b != 0:
        a, b = b, a % b
        end = timer()     
        measures_i.append(end-start)
        start = timer()
    end = timer() 
    measures_i.append(end-start)
    return {'mdc': a,'tempo': measures_i}

def mdc_recursive(a,b,start):
    if b == 0:
        end = timer()
        measures_r.append(end-start)
        return {'mdc': a,'tempo': measures_r}
    end = timer()
    measures_r.append(end-start)
    start = timer()
    return mdc_recursive(b,a%b,start)

def generate_numbers():
    t = (randint(100000000000,maxsize),randint(100000000000,maxsize))
    print('Numbers chosen: ',t)

    return t

def compare_measures(iterative_measures,recursive_measures,n):
    i, r = 0, 0
    for k in range(n):
        if iterative_measures[k] < recursive_measures[k]:
            i += 1
        else:
            r += 1

    filename = 'output.log'

    with open(filename,'w') as logfile:
        logfile.write(f'Number of times that iterative was faster: {i}\nNumber of times that recursive was faster: {r}\n')

def create_table_latex(iterative_measures,recursive_measures,n):
    fields = '\\hline\nExecuções & Iterative (s) & Recursive (s) \\\\ \n \\hline'
    filename = 'table.tex'

    with open(filename,'w') as texfile:
        texfile.write(fields + '\n')
        for k in range(n):
            texfile.write(f'{k+1} & {iterative_measures[k]} & {recursive_measures[k]} \\\\\n')
        
        texfile.write('\nIterativo:\n\ncoordinates {\n')

        for k in range(n):
            texfile.write(f'({k+1},{iterative_measures[k]})')

        texfile.write('\n};')

        texfile.write('\nRecursive:\n\ncoordinates {\n')

        for k in range(n):
            texfile.write(f'({k+1},{recursive_measures[k]})')

        texfile.write('\n};')    

def plot_graphs(x,y,name):
    plt.plot([*range(x)], y)
    plt.xlabel('Number of tests')
    plt.ylabel('Time (s)')
    plt.title(name)
    plt.show()


if __name__ == "__main__":
    t = (4857166715893011401, 1923838440290523428) # generate_tuple_list(n)

    di = mdc_iterative(t[0],t[1],timer())
    dr = mdc_recursive(t[0],t[1],timer())

    mdc_i = di['mdc']
    iterative_measures = di['tempo']
    mdc_r = dr['mdc']
    recursive_measures = dr['tempo']

    n = len(iterative_measures)
    # print(len(iterative_measures), len(recursive_measures))
    # print(iterative_measures,'\n\n', recursive_measures)

    compare_measures(iterative_measures,recursive_measures,n)
    create_table_latex(iterative_measures,recursive_measures,n)

    plot_graphs(n,iterative_measures,'Iterative Measures')
    plot_graphs(n,recursive_measures,'Recursive Measures')
