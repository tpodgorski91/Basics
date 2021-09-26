"""Write a program that categorizes each mail message by which day of the week the commit was done.
To do this look for lines that start with “From”,
then look for the third word and keep a running count of each of the days of the week.
At the end of the program print out the contents of your dictionary (order does not matter)."""


def imp_file():
    return open(r"D:\Maszt071\Python knownledge\Basics\strings\mails.txt")


def get_day():
    counts = {}
    file = imp_file()
    for line in file:
        if line.startswith("From "):
            line = line.strip()
            line = line.split()
            line = line[2]
            if counts.get(line, 0) == 0:
                counts[line] = 1
            else:
                counts[line] += 1
    print(counts)


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
    print(counts)


get_address()
get_day()
