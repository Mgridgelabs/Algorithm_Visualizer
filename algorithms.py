

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

sorting_algorithms = {
    "bubble": bubble_sort
}