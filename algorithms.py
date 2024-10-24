
#works by repeatedly swapping the adjacent elements if they are in the wrong order
def bubble_sort(arr):
    steps = [] 
    n = len(arr)
    
    for i in range(n):#iterates over each element in arrary
        for j in range(0, n-i-1):#compares adjacent elements
            steps.append(arr.copy())#stores current state of array
            if arr[j] > arr[j+1]:#if current element is > than the next one 
                arr[j], arr[j+1] = arr[j+1], arr[j]#swap elements
    steps.append(arr.copy())#stores final array state
    return steps

#finds the minimum element from unsorted part and swaps it with the first unsorted element
def selection_sort(arr):
    steps = []
    n = len(arr)
    
    for i in range(n):
        min_idx = i 
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps.append(arr.copy())
    return steps

#builds a sorted array by inserting elements one by one from unsorted potion into correct position
def insertion_sort(arr):
    steps = []
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1 
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            steps.append(arr.copy())
            arr[j + 1] = key
            steps.append(arr.copy())
    return steps


#divide the array into two halves, sort them and then merge them
def merge_sort(arr):
    steps = []
    def merge_sort_helper(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            merge_sort_helper(L)
            merge_sort_helper(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
                steps.append(arr.copy())

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
                steps.append(arr.copy())

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
                steps.append(arr.copy())
    merge_sort_helper(arr)
    return steps

#picks a pivot element from array and places it at the correct position in sorted array
def quick_sort(arr):
    steps = []
    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi-1)
            quick_sort_helper(arr, pi+1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                steps.append(arr.copy())
        arr[i+1], arr[high] = arr[high], arr[i+1]
        steps.append(arr.copy())
        return i + 1

    quick_sort_helper(arr, 0, len(arr)-1)
    return steps


# Builds a max-heap from the array, then repeatedly swaps the root of the heap with the last element and heapifies the reduced heap.
def heap_sort(arr):
    steps = []
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            steps.append(arr.copy())
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        steps.append(arr.copy())
        heapify(arr, i, 0)
    return steps

#An optimization of insertion sort, it sorts elements far apart and gradually reduces the gap between elements.
def shell_sort(arr):
    steps = []
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                steps.append(arr.copy())
            arr[j] = temp
            steps.append(arr.copy())
        gap //= 2
    return steps


sorting_algorithms = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort,
    "merge": merge_sort,
    "quick": quick_sort,
    "heap": heap_sort,
    "shell": shell_sort
}
