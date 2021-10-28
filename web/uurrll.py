import urllib.request, urllib.error, urllib.parse

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo-full.txt')
fhand2 = urllib.request.urlopen('http://data.pr4e.org/romeo-full.txt')


def up_to_3000(request):
    full_text = []
    for line in request:
        full_text.append(line.decode().strip())
    content = ' '.join(full_text)
    return content[:3000]


def count_char(request):
    char = {}
    for line in request:
        line = line.decode().strip()
        for word in line:
            if char.get(word, 0) == 0:
                char[word] = 1
            else:
                char[word] += 1
    return sum(char.values())


def blah(request):
    full_text = []
    for line in request:
        full_text.append(line.decode().strip())
    content = ' '.join(full_text)
    return content


# rng_char = up_to_3000(fhand)
unique_char = count_char(fhand2)
result = blah(fhand)