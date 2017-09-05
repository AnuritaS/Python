#Finding the most popular friend from dictionaries
'''Individual Student Friend Rating Score Dictionaries, (Construct a min of 10 student dictionaries)
Score 1 is lowest and Score of 5 is highest. Every student rates all the other students. So each dictionary has 9 elements.

Example with 3 students,
sam_friends = {“Bob”:3, “Raj”:5}
bob_friends = {“Sam”:5,”Raj”:1}
raj_friends = {“Sam”:3,”Bob”:5}

Find who has the highest score and that student is the most popular friend. Print the most popular friend and his/her score.'''

def famous():
    sam ={"Bob":3, "Raj":5, "adi":4,"anu":5,"bhanu":3,"eww":2,"hii":2,"am":1,"nonu":1}
    bob = {"Sam":5,"Raj":1,"adi":2,"anu":5,"bhanu":5,"eww":2,"hii":3,"am":1,"nonu":1}
    raj = {"Sam":3,"Bob":5,"adi":3,"anu":2,"bhanu":1,"eww":2,"hii":4,"am":1,"nonu":2}
    adi = {"Bob": 3, "Raj": 3, "Sam": 5, "anu": 2, "bhanu": 3, "eww": 4, "hii": 2, "am": 1, "nonu": 4}
    anu = {"Sam": 5, "Raj": 1, "adi": 2, "Bob": 5, "bhanu": 2, "eww": 5, "hii": 1, "am": 5, "nonu": 5}
    bhanu = {"Sam": 3, "Bob": 2, "adi": 3, "anu": 2, "Raj": 4, "eww": 3, "hii": 4, "am": 4, "nonu": 3}
    eww = {"Bob": 3, "Raj": 2, "adi": 4, "anu": 5, "bhanu": 3, "Sam": 1, "hii": 2, "am": 3, "nonu": 2}
    hii = {"Sam": 4, "Raj": 1, "adi": 2, "anu": 5, "bhanu": 5, "eww": 1, "Bob": 3, "am": 4, "nonu": 1}
    am = {"Sam": 2, "Bob": 5, "adi": 3, "anu": 2, "bhanu": 1, "eww": 2, "hii": 4, "Raj": 1, "nonu": 2}
    nonu = {"Sam": 1, "Bob": 1, "adi": 1, "anu": 3, "bhanu": 1, "eww": 2, "hii": 4, "am": 4, "Raj": 5}
    student=[sam,bob,raj,adi,anu,bhanu,eww,hii,am,nonu]
    star=dict.fromkeys(set().union(*student),0)
    for d in student:
        for key in d.keys():
            star[key]+=d[key]
    starvalue=max(star.values())
    for k,v in star.items():
        if(v==starvalue):
            starkid=k
    print("famous kid = ",starkid,"with score =",starvalue)
famous()