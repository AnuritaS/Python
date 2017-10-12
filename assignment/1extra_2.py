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
minh.heappush(12)
maxh.heappush(12)
maxh.heappush(22)
maxh.heappush(32)
maxh.heappush(1)
minh.heappush(44)
minh.heappush(56)
minh.heappush(8)
minh.heappush(4)
maxh.heappush(4)
# fetch "top" values

# fetch and remove "top" values
for i in range(len(minh)):
    print(minh.heappop(),maxh.heappop()) # "4 12"