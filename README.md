This code takes an array of numbers as input and returns the sorted array for each sorting algorithm. The algorithms are implemented as functions that take an array as input and return the sorted array.

Selection Sort:
Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the array and swapping it with the first element of the unsorted part. The process is repeated until all the elements are sorted. It has a time complexity of O(n^2) in the worst-case scenario, making it inefficient for large arrays.

Bubble Sort:
Bubble sort is also a simple sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order until the entire array is sorted. It compares each pair of adjacent elements and swaps them if they are in the wrong order. The process is repeated until no swaps are required, indicating that the array is sorted. The time complexity of bubble sort is also O(n^2) in the worst-case scenario, making it inefficient for large arrays.

Insertion Sort:
Insertion sort is a another simple sorting algorithm that builds the final sorted array one item at a time. It is much more efficient than the previous two algorithms for smaller arrays and partially sorted arrays. The algorithm works by assuming that the first element of the array is sorted and then inserting the next unsorted element into its correct position in the sorted part of the array. The time complexity of insertion sort is O(n^2) in the worst-case scenario, but it is O(n) in the best-case scenario when the array is already sorted.
