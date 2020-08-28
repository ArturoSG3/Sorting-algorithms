from random import randint
from Sorting_algorithms import bubbleSort, insertionSort, selectionSort, quickSort, mergeSort, heapSort, bucketSort

n = []
for i in range(10):
	n.append(randint(0,9999))
print("Input: ", n)
#print("Bubble sort: ", bubbleSort(n))
#print("Insertion sort: ", insertionSort(n))
#print("Selection sort: ", selectionSort(n))
#print("Quick sort: ", quickSort(n))
#print("Merge sort: ", mergeSort(n))
#print("Heap sort: ", heapSort(n))
print("Bucket sort: ", bucketSort(n))
