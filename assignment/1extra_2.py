'''
Get a list of number from the user (unsorted). Construct max and min heap from the unsorted list and output the list for min and max heap.
'''
import heapq
class MaxHeapObj(object):
  def __init__(self,val): self.val = val
  def __lt__(self,other): return self.val > other.val
  def __eq__(self,other): return self.val == other.val
  def __str__(self): return str(self.val)

class MinHeap(object):
  def __init__(self): self.h = []
  def heappush(self,x): heapq.heappush(self.h,x)
  def heappop(self): return heapq.heappop(self.h)
  def __getitem__(self,i): return self.h[i]
  def __len__(self): return len(self.h)

class MaxHeap(MinHeap):
  def heappush(self,x): heapq.heappush(self.h,MaxHeapObj(x))
  def heappop(self): return heapq.heappop(self.h).val
  def __getitem__(self,i): return self.h[i].val

minh = MinHeap()
maxh = MaxHeap()
# add some values
value = [x for x in input("Enter values:").split()]
for v in value:
  minh.heappush(v)
  maxh.heappush(v)

# fetch and remove "top" values
print('MinHeap and MaxHeap:')
for i in range(len(value)):
    print(minh.heappop(),'       ',maxh.heappop())