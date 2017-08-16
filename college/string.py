#to swap first and last letter of a string and make a new string
old=input("Enter string: ")
fst=old[:1]
len = len(old)
lst=old[len-1:]

new=lst+old[1:len-1]+fst
print("new string:",new)

#to remove all odd indexes' letters of a string
new1=""
for index in range(len):
    if index%2 == 0:
        new1=new1+old[index]
    else:
        print("removed:",old[index])
print("even index string:",new1)

#to find list of all words greater than n
old=input("Enter string: ")
n=eval(input("enter n:"))
list=old.split()
list1=dict()
for x in list:
    if len(x) > n:
        list1.append(x)
print(list1)

#to find the occurence of a word
c=0
for x in list:
    if x in list1:
        list1[x] +=1
    else:
        list1[x]=1
print(list1)

#add "ing" if length of a string is greater than 2 or "ly"
old=input("Enter string: ")
len = len(old)
new=""
if len>2:
    new=old+"ing"
else:
    new=old+"ly"
print(new)

#1204 UB
