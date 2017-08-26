#Get a list of numbers from the user, till he types “end”. Write two functions “bubble_sort” and “insertion_sort”, to sort the function using bubble sort and insertion sort. Arguments to the function would be user entered list. The function returns the sorted list according to the algorithm.

def bubble(a):
    length = len(a)
    for i in range(length):
        for j in range(length - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print("Bubble sorted:", a)

def insertion(a):
   length=len(a)
   for i in range(1,length):
       key=a[i]
       j=i-1
       while j>=0 and a[j]>key:
           a[j+1]=a[j]
           j-=1
       a[j+1]=key
   print("Insertion sorted:", a)

def sort():
    no=[]
    print("Enter numbers:")
    while True:
        l=input()
        if l=='end':
            break
        no.append(int(l))
    print("Unsorted list",no)
    bubble(no)
    insertion(no)

sort()