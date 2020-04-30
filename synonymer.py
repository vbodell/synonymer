from bs4 import BeautifulSoup
from urllib.request import urlopen

LINE_LIMIT = 80

query = input()
basurl = "http://www.synonymer.se/sv-syn/"
url = f"{basurl}{query}"
site = urlopen(url)
soup = BeautifulSoup(site, "html.parser")

synonymer = soup.find("div", id="dict-default").find("div", "body").ul.li.ol

rank = synonymer.find_all("li")
submeaning = synonymer.find_all("em")
synonym = synonymer.find_all("a")

i = 1
curLine = 0
for s in synonymer:
    if s in rank:
        print(f"\n{i}. {s.get_text()}", end='')
        i += 1
        curLine += 3 + len(s.get_text())

    elif s in synonym:
        if curLine + len(s.get_text()) > LINE_LIMIT:
            print()
            curLine = 0

        print(s.get_text(), end='')
        curLine += len(s.get_text())

        if s.next_sibling in rank:
            print()
            curLine = 0
        elif s.next_sibling in submeaning:
            pass
        else:
            print(", ", end='')
            curLine += 2

    elif s in submeaning:
        if curLine + len(s.get_text()) + 2 + len(s.next_sibling) > LINE_LIMIT:
            print()
            curLine = 0
        if s.previous_sibling in rank:
            print(f"{s.get_text()}: {s.next_sibling}", end='')
            curLine += len(s.get_text()) + 2 + len(s.next_sibling)
        else:
            print(f"\n{s.get_text()}: {s.next_sibling}", end='')
            curLine += len(s.get_text()) + 2 + len(s.next_sibling)
print()
