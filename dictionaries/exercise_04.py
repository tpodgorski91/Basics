""" Add code to the above program to figure out who has the most messages in the file.
 After all the data has been read and the dictionary has been created,
  look through the dictionary using a maximum loop
"""


def imp_file():
    return open(r"D:\Maszt071\Python knownledge\Basics\strings\mails.txt")


def get_address():
    counts = {}
    file = imp_file()
    for line in file:
        if line.startswith("From "):
            line = line.strip()
            line = line.split()
            line = line[1]
            if counts.get(line, 0) == 0:
                counts[line] = 1
            else:
                counts[line] += 1
    print(max(counts, key=counts.get), counts[max(counts, key=counts.get)])
    print(min(counts, key=counts.get), counts[min(counts, key=counts.get)])


get_address()

