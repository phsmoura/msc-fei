from random import randint
from timeit import default_timer as timer
from utils import *
from sort_algorithms import *


if __name__ == '__main__':
    size = 500
    max_random_number = 1000
    n = 50
    time_measure = {
        'bubble':[],
        'quick':[],
        'randomized_quick':[]
    }

    for k in range(n):
        array = generate_array(size,max_random_number)
        generate_log('Generated array: ', array, True)

        start_time = timer()
        bubble_array = bubble_sort(array)
        time_measure['bubble'].append(timer() - start_time)
        generate_log('Bubble sort: ', bubble_array, False)

        start_time = timer()
        quick_array = quick_sort(array, 0, size - 1)
        time_measure['quick'].append(timer() - start_time)
        generate_log('Quick sort pivot as the 1st position: ', quick_array, False)

        start_time = timer()
        quick_array = randomized_quick_sort(array, 0, size - 1)
        time_measure['randomized_quick'].append(timer() - start_time)
        generate_log('Quick sort pivot as a random position: ', quick_array, False)
        
    create_table_latex(time_measure['bubble'], time_measure['quick'], time_measure['randomized_quick'])

    create_coodinates_latex('bubble', time_measure['bubble'])
    create_coodinates_latex('quick', time_measure['quick'])
    create_coodinates_latex('randomized_quick', time_measure['randomized_quick'])

    plot_graphs(n, time_measure['bubble'], 'Bubblesort')
    plot_graphs(n, time_measure['quick'], 'Quicksort')
    plot_graphs(n, time_measure['randomized_quick'], 'Randomized Quicksort')