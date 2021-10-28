"""Exercise 4: Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved HTML document
 and display the count of the paragraphs as the output of your program. Do not display the paragraph text,
  only count them. Test your program on several small web pages as well as some larger web pages."""


def count_sth(address, sth):
    import requests
    from bs4 import BeautifulSoup
    i = 0
    r = requests.get(address)
    soup = BeautifulSoup(r.text, 'html.parser')
    for element in soup.find_all(sth):
        i += 1
    return i
