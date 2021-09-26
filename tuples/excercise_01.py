"""Read and parse the “From” lines and pull out the addresses from the line.
 Count the number of messages from each person using a dictionary.
After all the data has been read,
print the person with the most commits by creating a list of (count, email) tuples from the dictionary.
 Then sort the list in reverse order and print out the person who has the most commits."""


def imp_file():
    return open("mbox-long.txt")


def parse_mails():
    counts = {}
    file = imp_file()
    for line in file:
        if line.startswith("From "):
            line = line.strip()
            line = line.split()
            line = line[1]
            counts[line] = counts.get(line, 0) + 1
    return counts


def most_commits(slowik):
    return sorted([(v, k) for k, v in slowik.items()], reverse=True)[0]


slowik = parse_mails()
print(most_commits(slowik))
