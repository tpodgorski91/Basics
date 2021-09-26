"""This program counts the distribution of the hour of the day for each of the messages.
You can pull the hour from the “From” line by finding the time string and then splitting that string into parts
using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line,
 sorted by hour as shown below."""


def imp_file():
    return open(r"D:\Maszt071\Python knownledge\Basics\strings\mails.txt")


def parse_mails():
    counts = {}
    file = imp_file()
    for line in file:
        if line.startswith("From "):
            line = line.strip()
            line = line.split()
            hour = line[5]
            hour = hour.split(":")[0]
            counts[hour] = counts.get(hour, 0) + 1
    return counts


def most_commits(slowik):
    for k, v in sorted([(k, v) for k, v in slowik.items()]):
        print(k, v)


slowik = parse_mails()
most_commits(slowik)
