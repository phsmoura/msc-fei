from random import randint

def bubble_sort(array: list) -> list:
    for k in range(len(array)-1):
        for p in range(len(array) - k - 1):
            if array[p] > array[p+1]:
                aux = array[p]
                array[p] = array[p+1]
                array[p+1] = aux
    return array

def partition(array: list, start: int, end: int) -> int:
    pivot = array[start]
    x = start

    for y in range(start,end):
        if array[y] >= pivot:
            aux = array[x]
            array[x] = array[y]
            array[y] = aux
            x += 1
            

    aux = array[x]
    array[x] = array[end]
    array[end] = aux
    return x

def quick_sort(array: list, start: int, end: int) -> list:
    if start < end:
        partition_index = partition(array, start, end)
        quick_sort(array, start, partition_index - 1)
        quick_sort(array, partition_index, end)
    return array

def randomized_quick_sort(array: list, start: int, end: int):
    if start < end:
        partition_index = partition(array, randint(start, end), end)
        randomized_quick_sort(array, start, partition_index - 1)
        randomized_quick_sort(array, partition_index, end)
    return array