#Created by Arianna Conti

import datetime
date = datetime.date.today()

print("------------------------------------------------------------------\n"
      + "Arianna Conti\t\t\t\t\t " + str(date)
      + "\nCSCI 3351\t\t\t\t\t Word Completion\n"
      + "------------------------------------------------------------------\n")

#Ask the user for the name of a file that contains the text to analyze:
filename = input("Enter file that contains the text to analyze: ")
file = open(filename, "r")
worddict = {}
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
                if worddict.get(word) == None: #add to dictionary
                    worddict[word] = 1
                else :
                    worddict[word] = worddict[word] + 1 #increment int
file.close()
l = [None]*longest

for word in worddict :                          #FOR elements in dict
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


#file.close()

    #Second, add the word into a data structure that is keeping track of word information for the completion process. This data structure has 3 basic parts.
        #The top level part is a list that will have as many elements in it as the number of characters in the longest word seen so far. Each element in this list will be a dictionary which is indexed by the 26 letters of the alphabet.

        #The value for each entry in the dictionary will be a set of words. A word is added into this structure as follows.
            #The word is first added to the set contained in the dictionary corresponding to slot 0 in the list, indexed by the key of the first letter in the word.
            #Then, the second letter of the word is used to index into the dictionary corresponding to slot 1 in the list to add the word to that set. This continues for the remaining letters in the word.
#So this means that the word "help" would be added to the set of words that have an h as their first letter, the set having e as the second letter, the set for l as the third letter, and then p as the fourth letter.