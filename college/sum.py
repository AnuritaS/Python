class Sum:

    def add(self,a,b):
        return a+b


n1,n2 = eval(input("Enter two numbers to add:"))
obj = Sum()
print('Sum =',obj.add(n1,n2))
obj1 = Sum()
print('Sum =',obj1.add(2,3))

class List:
    def duplicate(self):
        sL = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e','']
        start=sL[0]
        eL =[]
        e = []
        e.append(start)
        for x in range(1,len(sL)):
            if(sL[x]==start):
                e.append(sL[x])
            else:
                eL.append(e)
                e = []
                start=sL[x]
                e.append(sL[x])
        return eL
obj2 = List()
print(obj2.duplicate())