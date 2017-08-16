from collections import Counter
def famous():
    sam = {"Bob":3, "Raj":5, "adi":4,"anu":5,"bhanu":3,"eww":2,"hii":2,"am":1,"nonu":1}
    bob = {"Sam":5,"Raj":1,"adi":2,"anu":5,"bhanu":5,"eww":2,"hii":3,"am":1,"nonu":1}
    raj = {"Sam":3,"Bob":5,"adi":3,"anu":2,"bhanu":1,"eww":2,"hii":4,"am":1,"nonu":2}
    adi = {"Bob": 3, "Raj": 3, "Sam": 5, "anu": 2, "bhanu": 3, "eww": 4, "hii": 2, "am": 1, "nonu": 4}
    anu = {"Sam": 5, "Raj": 1, "adi": 2, "Bob": 5, "bhanu": 2, "eww": 5, "hii": 1, "am": 5, "nonu": 5}
    bhanu = {"Sam": 3, "Bob": 2, "adi": 3, "anu": 2, "Raj": 4, "eww": 3, "hii": 4, "am": 4, "nonu": 3}
    eww = {"Bob": 3, "Raj": 2, "adi": 4, "anu": 5, "bhanu": 3, "Sam": 1, "hii": 2, "am": 3, "nonu": 2}
    hii = {"Sam": 4, "Raj": 1, "adi": 2, "anu": 5, "bhanu": 5, "eww": 1, "Bob": 3, "am": 4, "nonu": 1}
    am = {"Sam": 2, "Bob": 5, "adi": 3, "anu": 2, "bhanu": 1, "eww": 2, "hii": 4, "Raj": 1, "nonu": 2}
    nonu = {"Sam": 1, "Bob": 1, "adi": 1, "anu": 3, "bhanu": 1, "eww": 2, "hii": 4, "am": 4, "Raj": 5}
    star_student={"Sam": 0, "Bob": 0, "adi": 0, "anu": 0, "bhanu": 0, "eww": 0, "hii": 0, "am": 0, "Raj": 0,"nonu":0}
    dc=[sam,bob,raj]
    s=Counter(for x in dc)
    print(star_student)

famous()