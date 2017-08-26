#Get a list of non-empty tuples from the user. You can use any end of sequence representation for tuples and list. Write a function sort_tuple(). Input to the function is the list of tuples entered by the user. Output from the function is a sorted list according to the condition - sorted in increasing order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
#[(2, 2), (1, 3), (3, 4, 5), (1, 7)]

def sort_tuple(a):
    a.sort(key=lambda x:x[len(a)-1] )
    print("Sorted tuples",a)

def sort():
    no=[]
    print("Enter numbers:")
    while True:
        l=input()
        if l=='end':
            break
        no.append(tuple(int(x) for x in l.split(",")))
    print("Unsorted list",no)
    sort_tuple(no)

sort()

