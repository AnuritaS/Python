'''
1.	Files that have to be ready for the program – vocab.txt, stopwords.txt and book.txt. The file vocab.txt has a list of words. The file book.txt has a paragraph or a short story. The file stopwords.txt has the common words like - is, was, are, their, her, his etc. Your program should
a.	Remove the stop words from the content book.txt, referring to stopwords.txt.
b.	Find words from book.txt that are in vocab.txt. Find the frequency of occurrence of each word.
c.	Find the words from book.txt that are not in vocab.txt. List the words. Ask the user if these words could be added to vocab.txt.
d.	If the user enters yes, append the new words to vocab.txt, else end the program.
'''
import os
from collections import Counter
import re
stopw=open("./stopwords.txt", 'r+')
stopwlines = stopw.readlines()
for index in range(0, len(stopwlines)):
    stopwlines[index] = stopwlines[index].strip()
stopw.close()
bookw=open("./book.txt", 'r+')
bookwlines= bookw.readlines()
for index in range(0, len(bookwlines)):
    bookwlines[index] = bookwlines[index].strip()
bookex=open("./book.save.txt", 'w+')
bookw.close()
for bline in bookwlines:
    for sline in stopwlines:
        bline=bline.replace(sline,"")
    bookex.write(bline)
bookex.close()
choice=input("Do you want to replace words in stopwords.txt in book.txt (Yes/No)?")
if(choice == 'Yes' or choice =='yes' or choice=='YES'):
    os.remove("./book.txt")
    os.rename("./book.save.txt","./book.txt")
else:
    os.remove("./book.save.txt")
vocab=open("./vocab.txt","w+")
vocabdlines=vocab.readlines()
vocab.close()
for index in range(0, len(vocabdlines)):
    vocabdlines[index] = vocabdlines[index].strip()
words= re.findall(r'\w+', open('./book.txt').read().lower())
wordlist= Counter(words).most_common(100)
freqlist=[]
notexistinglist=[]
for word in vocabdlines:
    for (one,freq) in wordlist:
        if word==one :
            freqlist.append(freq)
            break
print("The frequency list is:")
for index in range(0,len(vocabdlines)):
    print("%s:%d" % (vocabdlines[index],freqlist[index]))
for (one,freq) in wordlist:
    existingbool=False
    for word in vocabdlines:
        if(word==one):
            existingbool=True
            break
    if(not existingbool):
        notexistinglist.append(one)
print("The words that do not exist in book.txt and exist in vocab.txt are: " , notexistinglist)
choicenext=input("Do you want to add these words to vocab.txt (Yes/No) ?")
vocab=open("./vocab.txt", 'a')
if (choicenext=='Yes' or choicenext=='yes' or choicenext== 'YES'):
    for word in notexistinglist:
        vocab.write(word+"\n")
vocab.close()
print(open("./vocab.txt",'r+').readlines())