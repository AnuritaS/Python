'''Write a parent class “Polygon”. This class has two attributes
no_of_sides  - represent the number of sides . This is passed as argument to the constructor when the object is getting created.
sides – is a list representing the value of the sides, initialise the value of sides to 0 in constructor
The class has two methods
input_sides() – Gets the sides from the user. This method would display messages like
“Enter the value for side1”
“Enter the value for side2”
….
“Enter the value for siden”
and gets the values for the sides from the user and populates the list.
print_sides() – Prints the values of the sides
Create a child class called Triangle, that calls the Parent class constructor with 3 as the number of sides. The child class has one additional method “findArea”, that finds the area of the triangle using the formula – (side1+side2+side3)/2
'''
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



