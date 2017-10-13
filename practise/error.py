import sys
import random
import numpy as np

def safe(obj):
    try:
        ret=float(obj)
    except ValueError:
        ret='could not convert non_number'
    except TypeError:
        ret='object type cannot be converted to float'
    else:
        ret='no error'
    return ret


matrix = [[random.randint(0,1) for x in range(4)]for y in range(4)]
c = 0;
maxRow = 0;
for row in matrix:
    if (row.count(1) >= c):
        c = row.count(1);
        maxRow = matrix.index(row);
    for value in row:
      print(value, end=" ")
    print()
print("largest row",maxRow)
v = np.array(matrix)
print(v[:,[0,1]])




def func():
    global x
    print('x is', x)
    x = 2
    print('Changed global x to', x)
x = 50
func()
print('Value of x is', x)

