#Get a string as input from the user and the sub string to be searched also from the user. Find and list the index positions of the sub string and also the number of occurrences of the sub string.

def sub():
    s=input("Enter a string \n")
    sub=input("Enter substring \n")
    l=s.split(" ")
    print("Occurences", s.count(sub))

    for x in range(len(l)):
        if l[x] == sub:
            print("index:",x)



sub()