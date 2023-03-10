This code takes an array of numbers as input and returns the sorted array for each sorting algorithm. The algorithms are implemented as functions that take an array as input and return the sorted array.

Selection Sort:
Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the array and swapping it with the first element of the unsorted part. The process is repeated until all the elements are sorted. It has a time complexity of O(n^2) in the worst-case scenario, making it inefficient for large arrays.

Bubble Sort:
Bubble sort is also a simple sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order until the entire array is sorted. It compares each pair of adjacent elements and swaps them if they are in the wrong order. The process is repeated until no swaps are required, indicating that the array is sorted. The time complexity of bubble sort is also O(n^2) in the worst-case scenario, making it inefficient for large arrays.

Insertion Sort:
Insertion sort is a another simple sorting algorithm that builds the final sorted array one item at a time. It is much more efficient than the previous two algorithms for smaller arrays and partially sorted arrays. The algorithm works by assuming that the first element of the array is sorted and then inserting the next unsorted element into its correct position in the sorted part of the array. The time complexity of insertion sort is O(n^2) in the worst-case scenario, but it is O(n) in the best-case scenario when the array is already sorted.

Merge Sort:
Merge sort is a divide and conquer algorithm for sorting arrays. The basic idea behind the algorithm is to divide the array into two halves, sort each half recursively, and then merge the two sorted halves back into a single sorted array. The merging process is done by comparing the first element of each subarray and taking the smaller one, repeating the process until both subarrays are merged. The time complexity of merge sort is O(n log n) in the average and worst-case scenarios, making it more efficient than selection sort and bubble sort for large arrays.

Quick Sort:
Quick sort is also a divide and conquer algorithm for sorting arrays. It works by selecting a pivot element from the array and partitioning the other elements into two subarrays, according to whether they are less than or greater than the pivot. The subarrays are then sorted recursively. The pivot selection and partitioning processes result in a well-balanced distribution of elements, leading to efficient sorting. The time complexity of quick sort is O(n log n) in the average case, but it can be as slow as O(n^2) in the worst-case scenario, when the pivot is always the largest or smallest element. To avoid the worst-case scenario, a random pivot selection or a pivot selection algorithm that guarantees a balanced distribution is used in practice.
