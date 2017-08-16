n=eval(input("Enter rows"))
m=eval(input("Enter columns"))
mat=[]
for row in range(n):
    mat.append([])
    for col in range(m):
        el=eval(input("Enter element:"))
        mat[row].append(el)

print(mat)
n1=eval(input("Enter rows"))
m1=eval(input("Enter columns"))
mat1=[]
for row in range(n1):
    mat1.append([])
    for column in range(m1):
        el=eval(input("Enter element:"))
        mat1[row].append(el)

print(mat1)
mat2=[[0 for col in range(len(mat1[0]))]for row in range(len(mat))]
for row in range(len(mat)):
    for col in range(len(mat1[0])):
        for k in range(len(mat1)):
          mat2[row][col]+=mat[row][k]*mat1[k][col]
print(mat2)
print()
#print(mat2)