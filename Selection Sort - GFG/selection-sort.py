#User function Template for python3

class Solution: 
    
    def __init__(self):
        pass
    
    def select(self, arr, i):
        
        smallest = arr[i]
        
        for it in range(len(arr))  :
            
            if arr[it] < smallest:
                smallest = arr[it]
        
        return smallest  
    
    def selectionSort(self, arr,n):
        
        new_a = []
        count = 0
        
        
        for x in range(n):
            smallest = self.select(arr, i = count)
            new_a.append(smallest)
            del arr[arr.index(smallest)]
        
        for arras in new_a:
            arr.append(arras)
        return arr
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends