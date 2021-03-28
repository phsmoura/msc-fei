from random import randint

def bubble_sort(array: list) -> list:
    for k in range(len(array)-1):
        for p in range(len(array) - k - 1):
            if array[p] > array[p+1]:
                aux = array[p]
                array[p] = array[p+1]
                array[p+1] = aux
    return array

def partition(array: list, start: int, end: int, pivot: int) -> int:
    while start <= end:
        while array[start] < pivot:
            start += 1

        while array[end] > pivot:
            end -= 1

        if start <= end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1
    return start

def quick_sort(array: list, start: int, end: int) -> list:
    if start < end:
        pivot = array[start]
        partition_index = partition(array, start, end, pivot)
        quick_sort(array, start, partition_index - 1)
        quick_sort(array, partition_index, end)
    return array

def randomized_quick_sort(array: list, start: int, end: int):
    if start < end:
        random_position = randint(start, end-1)
        pivot = array[random_position]
        partition_index = partition(array, start, end, pivot)
        randomized_quick_sort(array, start, partition_index - 1)
        randomized_quick_sort(array, partition_index, end)
    return array