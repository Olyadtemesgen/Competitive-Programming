#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        current = i
        while current * 2 + 1 < n:
            
            if current* 2 + 2 < n and \
            arr[current* 2 + 2] >= arr[current * 2 + 1] and arr[current* 2 + 2] >= arr[current]:
                
                arr[current* 2 + 2], arr[current] = arr[current], arr[current* 2 + 2]
                current = current * 2 + 2
            
            elif arr[current* 2 + 1] > arr[current]:
            
                arr[current* 2 + 1], arr[current] = arr[current], arr[current* 2 + 1]
                current = current * 2 + 1
            
            else:
                break
        
        return arr
        
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for x in range(len(arr) - 1, -1, -1):
            self.heapify(arr, n, x)
            # print(arr)
        return arr
    #Function to sort an array using Heap Sort.    
    
    def HeapSort(self, arr, n):
        
        self.buildHeap(arr, n)
        
        index = len(arr) - 1
        
        for x in range(n):
            
            arr[0], arr[index] = arr[index], arr[0]
            self.heapify(arr, index, 0)
            index -= 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)
