""" This program records the domain name (instead of the address) where the message was sent from instead
of who the mail came from (i.e., the whole email address).
At the end of the program, print out the contents of your dictionary.
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
            line = line.split("@")
            line = line[1]
            if counts.get(line, 0) == 0:
                counts[line] = 1
            else:
                counts[line] += 1
    print(max(counts, key=counts.get), counts[max(counts, key=counts.get)])
    print(min(counts, key=counts.get), counts[min(counts, key=counts.get)])


get_address()

