# ... Importing the necessary libraries

import matplotlib.pyplot as plt
import string


# ... Setting up the figure

fig = plt.figure("Acceleration")
ax = fig.add_subplot(111)


# ... Reading the file and splitting between words

file = open("Frankenstein.txt")
wordList = file.read().split()


# ... Eliminating punctuation

wordList = [''.join(c for c in s if c not in string.punctuation).lower() for s in wordList]


# ... Counting the frequency of each word

wordFreq = [wordList.count(word) for word in wordList]


# ... Given a list of words, return a dictionary of
# word-frequency pairs

def wordListToFreqDict(wordList):

    # ... Counting the frequency of each word

    wordFreq = [wordList.count(p) for p in wordList]

    # ... Pairing and then sorting the list of word frequencies

    pairedDict = dict(zip(wordList, wordFreq))
    sortedList = sorted(pairedDict.items(), reverse=True, key=lambda x: x[1])

    # ... Creating the empty arrays which will then be
    # ... used to contain the words and their values

    valuesArray = []
    keysArray = []

    print "\nPairs:\n"
    for pair in sortedList:
        print pair

        for word in pair:
            if type(word) == int:
                valuesArray.append(word)
            else:
                keysArray.append(word)

        print "\n"

    print "Sorted List:\n", sortedList

    print "\nValues Array:\n", valuesArray
    print "\nKeys Array:\n", keysArray

    ax.barh(keysArray, valuesArray)
    plt.show()


# ... Calling the program

wordListToFreqDict(wordList)


# ... Showing the histogram

plt.show()
