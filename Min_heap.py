class MinHeap: 
	def __init__(self, array):
		self.min_heap = array
		self.capacity = len(array)
		self.buildHeap()

	#Parent of a node.
	def parent(self, i): 
		return (i-1)//2

	#Left child of a node.
	def left(self, i):
		if 2*i + 1 < self.capacity:
			return 2*i + 1
		return None

	#Right child of a node.
	def right(self, i): 
		if 2*i + 2 < self.capacity:
			return 2*i + 2
		return None

	#Build the min-heap.
	def buildHeap(self):
		none_leaf_nodes = self.capacity//2 - 1
		
		#Loop to verify all nodes that are not a leaf.
		for i in range(none_leaf_nodes, -1, -1):
			self.minHeapify(i)

	#Returns minimum element and deletes it.
	def min(self):
		minimum = self.min_heap[0]
		self.delete()
		return minimum

	#Verify the position on the heap for one element.
	def minHeapify(self, i):
		smallest = i
		left = self.left(i)
		right = self.right(i)

		#Find the smallest between parent and children.
		if left:
			if self.min_heap[smallest] > self.min_heap[left]:
				smallest = left
		if right:
			if self.min_heap[smallest] > self.min_heap[right]:
				smallest = right

		#Change the smallest if it is not the parent.
		if smallest != i:
			self.min_heap[smallest], self.min_heap[i] = self.min_heap[i], self.min_heap[smallest]
			self.minHeapify(smallest)
	
	#Inserts an element to the heap.
	def insert(self, element):
		self.min_heap.append(element)
		self.capacity += 1
		i = (self.capacity - 1)

		#Verify the correct position of the new element.
		while i > 0:
			parent = self.parent(i)
			if self.min_heap[i] < self.min_heap[parent]:
				self.min_heap[i], self.min_heap[parent] = self.min_heap[parent], self.min_heap[i]
			else: 
				break
			i = parent
	
	#Delete the minimum element and correct the heap. 
	def delete(self):
		self.min_heap[0] = self.min_heap[self.capacity - 1]
		self.min_heap.pop()
		self.capacity -= 1
		self.minHeapify(0)
			