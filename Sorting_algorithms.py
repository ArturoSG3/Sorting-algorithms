from Min_heap import MinHeap
def quickSort(nums):
	#Check if empty.
	if(len(nums) <= 1):
		return nums
	left = []
	right = []
	pivot = nums[0]
	#Sort pivot.
	for i in range(1, len(nums)):
		if(pivot > nums[i]): 
			left.append(nums[i])
		else: 
			right.append(nums[i])
	return quickSort(left) + [pivot] + quickSort(right)

def bubbleSort (nums):
	for i in range(len(nums)-1):
		swapped = False
		#Move largest to the last position.
		for j in range(len(nums)-i-1):
			if(nums[j] > nums[j+1]): 
				nums[j], nums[j+1] = nums[j + 1], nums[j]
				swapped = True
		#Verify if elements are already sorted.
		if not swapped:
			return nums
	return nums

def insertionSort (nums):
	for i in range(1, len(nums)):
		tmp = nums[i]
		j = i-1 
		#Move sorted elements.
		while(j>=0 and nums[j] > tmp):
			nums[j+1] = nums[j]
			j -= 1
		#Insert element.
		nums[j+1] = tmp
	return nums

def selectionSort (nums): 
	for i in range(len(nums)): 
		minimum = i
		#Find the minimum element.
		for j in range(i+1, len(nums)): 
			if nums[j] < nums[minimum]: 
				minimum = j
		#Swap elements if the minimum is different than current.
		if minimum != i: 
			nums[minimum], nums[i] = nums[i], nums[minimum]
	return nums


def bucketSort(nums):
	buckets = {}
	maximum = max(nums)
	buckets = []
	#Build the bucket list.
	for i in range(10):
		buckets.append([])
	digits = 0
	#Find digits of the maximum element.
	while maximum > 0: 
		maximum = maximum//10
		digits += 1
	print(digits)
	#Place numbers in buckets.
	for n in nums: 
		i = n//(10**(digits-1))
		buckets[i].append(n)
	merged = []
	#Sort each bucket and merge them.
	for bucket in buckets:
		mergeSort(bucket)
		merged += bucket
	return merged

def mergeSort(nums):

	#Split into sublists and send them to merge. 
	def divide(start, end):
		if start < end: 
			mid = (end-start)//2 + start
			divide(start, mid)
			divide(mid+1, end)
			merge(start, mid, end)
	
	#Merge two ordered lists. 
	def merge(start, mid, end): 
		i = start
		j = mid+1
		sorted_nums = []
		#Find the smallest element in one list and add them to the sorted list. 
		while i<=mid and j<=end:
			if nums[i]<= nums[j]:
				sorted_nums.append(nums[i])
				i+= 1
			else:
				sorted_nums.append(nums[j])
				j+= 1
		#Add the remaining elements to the sorted list. 
		while j <= end:
				sorted_nums.append(nums[j])
				j+= 1
		while i<= mid:
				sorted_nums.append(nums[i])
				i += 1
		nums[start:end+1] = sorted_nums


	divide(0, len(nums)-1)
	return nums

def heapSort(nums):
	#Uses min-heap to sort the array. 
	heap = MinHeap(nums)
	sorted_array = []
	for i in range(len(nums)):
		sorted_array.append(heap.min())
	return sorted_array



