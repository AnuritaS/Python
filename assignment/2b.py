def sub():
    s=input("Enter a string \n")
    sub=input("Enter substring \n")
    l=s.split(" ")
    print("Occurences", s.count(sub))

    for x in range(len(l)):
        if l[x] == sub:
            print("index:",x)



sub()