class MaxHeap:

    def __init__(self, n):
        self.n = n
    
    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2
    
    def max_heap(self, a, n, i):
        l = self.left(i)
        r = self.right(i)

        if l < n and a[l] > a[i]:
            largest = l
        else:
            largest = i

        if r < n and a[r] > a[largest]:
            largest = r
    
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            self.max_heap(a, n, largest)
    

 
a = list(map(int, input("Enter the numbers you want to sort: ").rstrip().split()))
n = len(a)
maxHeap = MaxHeap(n)

for i in range(n, -1, -1):
    maxHeap.max_heap(a, n, i)
 
for i in range(n-1, 0, -1):
    a[0], a[i] = a[i], a[0]
    maxHeap.max_heap(a, i, 0)

print(a)
