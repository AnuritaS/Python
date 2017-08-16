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

