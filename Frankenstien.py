import string

file = open("Frankenstein.txt")
wordList = file.read().split()

wordList = [''.join(c for c in s if c not in string.punctuation).lower() for s in wordList]

wordFreq = [wordList.count(word) for word in wordList]

# Given a list of words, return a dictionary of
# word-frequency pairs


def wordListToFreqDict(wordList):
    wordFreq = [wordList.count(p) for p in wordList]

    pairedDict = dict(zip(wordList, wordFreq))
    sortedDict = sorted(pairedDict.items(), reverse=True, key=lambda x: x[1])

    print("Words dictionary\n", sortedDict, "\n")


"""
# Debugging

print "String\n", file, "\n"
print "List\n", str(wordList), "\n"
print "Frequencies\n", str(wordFreq), "\n"
print "Pairs\n", str(zip(wordList, wordFreq)), "\n"
"""

wordListToFreqDict(wordList)

a = []
count = 0

for word in wordList:
    if word not in a:
        a.append(word)
        count += 1
    print count
