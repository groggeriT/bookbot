import sys
from stats import numOfWords, characterCount, characterSort, sortOn

# to open and read books from books/
def getBookText(filePath):
    with open(filePath) as f:
        fileContents = f.read()
    return fileContents

# Main function ig
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
        
    # relevant variables that are a big ol pain in my ass
    path = sys.argv[1]
    text = getBookText(path)
    length = numOfWords(text)
    character = characterCount(text)
    sortDict = characterSort(character)
    sortDict.sort(reverse = True, key = sortOn)


    # the main meat of this function
    print("============ BOOKBOT ============")
    print(f"Analyzin book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {length} total words")
    print("--------- Character Count -------")
    for i in sortDict:
        print(f"{i["char"]}: {i["num"]}")
    return

main()