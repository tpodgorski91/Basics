def test():
    """Create a list of unique words, which will contain the final result.
    Write a program to open the file romeo.txt and read it line by line.
    For each line, split the line into a list of words using the split function.
    For each word, check to see if the word is already in the list of unique words.
    If the word is not in the list of unique words, add it to the list.
    When the program completes, sort and print the list of unique words in alphabetical order."""

    i = 0
    vocab = list()
    file = open("romeo.txt")
    stuff = [line.split() for line in file]
    for sentence in stuff:
        for word in sentence:
            if word not in vocab:
                vocab.append(word)
            else: continue
    vocab.sort()
    return vocab


result = test()
print(result)
