class Polygon:
    no_side=0
    sides=[]
    def __init__(self,no_side):
        self.no_side=no_side
        self.sides = [x for x in range(self.no_side)]
        for i in self.sides:
         i=0

    def input_sides(self):
        for i in range(len(self.sides)):
            self.sides[i]=eval(input("Enter value of side%d " % (i)))

    def print_sides(self):
        print(self.sides)

#p=Polygon(0)


class Triangle(Polygon):
    def __init__(self,no_sides):
        super(Triangle,self).__init__(no_sides)

    def findArea(self):
        area=0
        for i in self.sides:
            area+=i
        print("Area is:",area/2)

t=Triangle(3)
t.input_sides()
t.print_sides()
t.findArea()



