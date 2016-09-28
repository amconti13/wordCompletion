#Created by Arianna Conti

import datetime
date = datetime.date.today()
longest = 0

print("\n--------------------------------------------------------------------",
      "\nArianna Conti\t\t\t\t\t ", str(date),
      "\nCSCI 3351\t\t\t\t\t Word Completion\n",
      "\n--------------------------------------------------------------------",
      "\nThis program takes a file and the start of a word and returns the",
      "\nlikely set of completed words and the percentage of how likely each ",
      "\nword is the proper completion.")

#-------------------------------------------------------------------------------
#Read in and return lines from file
def get_datalines(filename = "" ) :
    if not filename :
        filename = input("\nEnter file that contains the text to analyze: ")
    file = open(filename, "r")
    listOfLines = file.readlines()
    file.close()
    return listOfLines

#-------------------------------------------------------------------------------
#Split the line into words and clean them up
def clean(line) :
    for word in line.split():
        word = word.strip(",.?!'\"()#$@^&*<>{}[]|_+-=")
        word = word.upper()
        yield word

#-------------------------------------------------------------------------------
#Make dictionary of words and the amount it shows up
def get_wordCountDict( lines ) :
    global longest
    wc = {}                                         #wordcount dictionary
    for line in lines :                             #FOR each line
        for w in clean(line) :                      #FOR each clean word
            for wl in (len(l) for l in w.split()):  #word length
                if wl > longest :                   #get longest word length
                   longest = wl
                if wl > 1 :                         #IF word is longer than 1
                    if wc.get(w) == None:           #IF not in dictionary
                        wc[w] = 1                   #Add to dictionary
                    else :                          #Increment number associated
                        wc[w] = wc[w] + 1           #   with word in dictionary
    return wc

#-------------------------------------------------------------------------------
#List of Dicitonaries
def get_listOfDictionaries(wordCountDictionary) :
    global longest
    l = [None]*longest
    for word in wordCountDictionary :               #FOR elements in dict
        letters = list(word)
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
    return l

#-------------------------------------------------------------------------------
#Intersects the two lists
def intersect(list1, list2) :
    list = []
    for x in range(0,len(list1)):
        for y in range(0,len(list2)):
            if list1[x] == list2[y]:
                list.append(list1[x])
    return list

#-------------------------------------------------------------------------------
#Dictionary with possible words and possibility percentage
def getWordPossibility(wc, w) :
    t = 0
    for i in range(0, len(w)) :                     #FOR all the possible words
        t = wc[w[i]] + t                            #Total up amount of words
    for i in range(0,len(w)) :                      #FOR all the possible words
        possDict[w[i]] = ((wc[w[i]] / t) * 100)     #Make dict with word and %
    return possDict

#-------------------------------------------------------------------------------
lines = get_datalines( )
wordcount = get_wordCountDict( lines )
l = get_listOfDictionaries( wordcount )

cont = 'y'
possWords = []                                      #possible words

while cont == 'y' :
    possDict = {}                                   #possibility dictionary
    
    part = input( "\nEnter a starting portion of a word: " )
    part = list( part.upper() )
    
    for i in range(0, len(part)) :                  #FOR each letter from input
        if i == 0 :                                 #IF first letter
            possWords = l[i][part[i]]               #Make list of possible words
        else:                                       #ELSE narrow list by
            possWords = intersect(l[i][part[i]], possWords) #list intersection

    possDict = getWordPossibility(wordcount, possWords) #Make final dictionary
    sortedPoss = sorted(possDict, key=possDict.__getitem__,reverse = True)

    print()                                         #print
    for i in range(0, 5) :
        if len(sortedPoss) == i :
            break
        print(round(possDict[sortedPoss[i]]), "% ",
              "chance the word is", sortedPoss[i])
            #look up set width
    cont = input("\nAgain?(y/n): ")

#Sort by key:
#sorted(wordcount, key=wordcount.__getitem__, reverse = True)
#Found:http://pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/

