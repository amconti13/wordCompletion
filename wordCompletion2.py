#Created by Arianna Conti

import datetime
date = datetime.date.today()

print("------------------------------------------------------------------\n"
      + "Arianna Conti\t\t\t\t\t " + str(date)
      + "\nCSCI 3351\t\t\t\t\t Word Completion\n"
      + "------------------------------------------------------------------\n")
def intersect(list1, list2) :
    #print("List 1: ", list1)
    #print("List 2: ", list2)
    list = []
    for x in range(0,len(list1)):
        for y in range(0,len(list2)):
            # print(list1[x])
            #print(list2[x])
            if list1[x] == list2[y]:
                list.append(list1[x])
    return list
#-------------------------------------------------------------------------------

#Ask the user for the name of a file that contains the text to analyze:
filename = input("Enter file that contains the text to analyze: ")
file = open(filename, "r")
wordcount = {}
longest = 0
#Open the file and read the lines of text:
for line in file :
    
    #Break each line into words:
    wordlist = line.split()

    #Strip out all of the special symbols:
    for index in range(0, len(wordlist)) : #for the length of the wordlist
        word = wordlist[index]
        word = word.strip(",.?!'\"()#$@^&*<>{}[]|_+-=")
        word = word.upper() #can do either lower or upper
        
        #For length of word
        for wordlen in (len(wordlen) for wordlen in word.split()):
            if wordlen > longest : #calculate length of longest word
                longest = wordlen
            
            if wordlen > 1 :
                if wordcount.get(word) == None: #add to dictionary
                    wordcount[word] = 1
                else :
                    wordcount[word] = wordcount[word] + 1 #increment int
file.close()

#wordcount = sorted(wordcount, key=wordcount.__getitem__, reverse = True)
#http://pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/
l = [None]*longest

for word in wordcount :                          #FOR elements in dict
    letters = list(word)                        #make word into list
    
    for i in range(0,len(letters)) :            #FOR letters in word
        if l[i] == None :                       #IF no dictionary
            words = [word]                      #make list
            l[i] = {letters[i]: words }         #create dictionary
        
        else:                                   #ELSE
            temp = l[i]                         #temp dict to manipulate
            if letters[i] in temp :             #IF key already exists
                words = temp[letters[i]]        #list of existing words
                words.append(word)              #append new word
                temp.update({letters[i]:words}) #update dict element
            else:                               #ELSE
                temp[letters[i]] = [word]       #add dict element
            l[i] = temp                         #save final dict into list
#print(l[i])
#-------------------------------------------------------------------------------
#Step 2 - Word completion
cont = 'y'
possibleChoices = []
while cont == 'y' :
    possDict = {}
    part = input("Starting portion of word: ")
    partlist = list(part.upper())
    for i in range(0,len(partlist)) :
        if i == 0:
            possibleChoices = l[i][partlist[i]]
        else:
            possibleChoices = intersect(l[i][partlist[i]], possibleChoices)
    #print(possibleChoices)
    total = 0
    for i in range(0, len(possibleChoices)) :
        total = wordcount[possibleChoices[i]] + total
    for i in range(0,len(possibleChoices)) :
        possDict[possibleChoices[i]] = ((wordcount[possibleChoices[i]]/total)*100)
#print(possDict)
        
    inOrderPoss = sorted(possDict, key=possDict.__getitem__,reverse = True)
#print(possDict)
    for i in range(0, 5) :
        if len(inOrderPoss) == i :
            break
        print(round(possDict[inOrderPoss[i]]), "% chance the word is", inOrderPoss[i])
    cont = input("Again?(y/n): ")




