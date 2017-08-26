#Define a class named “Time”, with instance attributes hours, minutes and seconds. The class consists of below method, apart from constructor
'''input_values() – Gets the values of attributes from the user.
print_details() – Prints the values of the attributes

Overload the operators “+” and “-“ to add and subtract the corresponding attribute values and print accordingly.'''

import math
class Time:
    hr=0
    min=0
    sec=0
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec


    def input_values(self):
        self.hr = eval(input("Enter hour \n"))
        self.min = eval(input("Enter a minutes \n"))
        self.sec = eval(input("Enter a seconds \n"))

    def __add__(self, other):
        hr=self.hr+other.hr
        min = self.min + other.min
        sec = self.sec + other.sec
        return Time(hr, min, sec)

    def __sub__(self, other):
        hr = self.hr - other.hr
        min = self.min - other.min
        sec = self.sec - other.sec
        return Time(hr, min, sec)


    def __str__(self):
        if self.sec>60:
            self.min+=1
            self.sec=self.sec-60
        if self.min>60:
            self.hr+=1
            self.min=self.min-60
        if self.hr>24:
            self.hr=self.hr-24
        if self.sec < 0:
            self.sec = 60 + self.sec
            self.min -= 1
        if self.min<0:
            self.min=60+self.min
            self.hr-=1
        if self.hr < 0:
            self.hr =  -self.hr


        return str(self.hr) + ":" + str(self.min) + ":" + str(self.sec)

    def print_details(self,add,sub):
        print("t1+t2=",add)
        print("t1-t2=",sub)

t1=Time(20,18,31)
t2=Time(14,53,12)

t1.input_values()
t2.input_values()
ad=t1+t2
su=t1-t2

t1.print_details(ad,su)

