def mail_parser():
    """Write a program to read through the mail box data and when you find line that starts with “From”,
     you will split the line into words using the split function. We are interested in who sent the message,
      which is the second word on the From line."""

    stuff = list()
    file = open("mails.txt")
    for line in file:
        line = line.strip()
        if line.startswith("From"):
            line = line.split()
            if line[1] not in stuff:
                stuff.append(line[1])
    print(f"There were {len(stuff)} mail addresses found.")
    return stuff


result = mail_parser()
print(result)