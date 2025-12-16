# to determine the number of words in a given text
def numOfWords(bookText):
    words = bookText.split()
    wordCount = len(words)
    return wordCount

# catagorising every individual letter and punctuation into a dictionary and assigning the value of how often it has appeared. 
def characterCount(bookText):
    charCount = {}
    lower = " "
    for char in bookText:
        lower = char.lower()
        if lower in charCount:
            charCount[lower] += 1
        else:
            charCount[lower] = 1
    return charCount

# sorting the above dictionary into a report ig
def characterSort(charCount):
    characters = []
    for char, num in charCount.items():
        if char.isalpha() == True:
                charDict = {}
                charDict["char"] = char
                charDict["num"] = num
                characters.append(charDict)
    return characters
    
# to actually sort the above mess of shit
def sortOn(items):
    return items["num"]
