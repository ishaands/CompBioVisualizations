#helper functions for algorithms and flask server

def minArr(arr):
    min = 1000000000
    for i in range(len(arr)):
        if (arr[i] < min):
            min = arr[i]
    
    return min

def maxArr(arr):
    max = 0 
    for i in range(len(arr)):
        if (arr[i] < max):
            max = arr[i]
    
    return max    