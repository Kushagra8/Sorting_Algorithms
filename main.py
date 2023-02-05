# Python program for implementation of various sorting algorithms

def selection_sort(arr):
    """
    Selection sort algorithm implementation
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    """
    Insertion sort algorithm implementation
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bubble_sort(arr):
    """
    Bubble sort algorithm implementation
    """
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_sort(arr):
    """
    Merge sort algorithm implementation
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def partition(arr, low, high):
    """
    Helper function for quick sort algorithm
    """
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    """
    Quick sort algorithm implementation
    """
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr


def test_sorting_algorithms():
    arr = [64, 25, 12, 22, 11]
    assert selection_sort(arr) == [11, 12, 22, 25, 64]
    assert bubble_sort(arr) == [11, 12, 22, 25, 64]
    assert insertion_sort(arr) == [11, 12, 22, 25, 64]
    assert merge_sort(arr) == [11, 12, 22, 25, 64]
    assert quick_sort(arr) == [11, 12, 22, 25, 64]

    arr = [1, 2, 3, 4, 5]
    assert selection_sort(arr) == [1, 2, 3, 4, 5]
    assert bubble_sort(arr) == [1, 2, 3, 4, 5]
    assert insertion_sort(arr) == [1, 2, 3, 4, 5]
    assert merge_sort(arr) == [1, 2, 3, 4, 5]
    assert quick_sort(arr) == [1, 2, 3, 4, 5]

    arr = [5, 4, 3, 2, 1]
    assert selection_sort(arr) == [1, 2, 3, 4, 5]
    assert bubble_sort(arr) == [1, 2, 3, 4, 5]
    assert insertion_sort(arr) == [1, 2, 3, 4, 5]
    assert merge_sort(arr) == [1, 2, 3, 4, 5]
    assert quick_sort(arr) == [1, 2, 3, 4, 5]

    arr = [1]
    assert selection_sort(arr) == [1]
    assert bubble_sort(arr) == [1]
    assert insertion_sort(arr) == [1]
    assert merge_sort(arr) == [1]
    assert quick_sort(arr) == [1]


test_sorting_algorithms()