'''
Represent a matrix as nested lists. Get number of rows, number of columns and input elements from the user and represent it as matrix.
Also, since the matrix is a sparse matrix, represent it using a dictionary. Construct the dictionary.
            Example
	mtx = {(0,3): 1, (2, 1): 2, (4, 3): 3}
a.	The dictionary has entries for non-zero elements
b.	Key is a tuple that holds the row and column index
c.	Value is the element
'''
n=eval(input("Enter rows"))
m=eval(input("Enter columns"))
mat=[]
mat_dict={}
for row in range(n):
    mat.append([])
    for col in range(m):
        el=eval(input("Enter element:"))
        mat[row].append(el)
        if(el!=0):
            mat_dict[(row,col)]=el

print(mat)

print(mat_dict)