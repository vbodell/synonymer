from __future__ import print_function
from bs4 import BeautifulSoup
import urllib

query = raw_input()
basurl = "http://www.synonymer.se/?query="
url = "%s%s" % (basurl, query)
site = urllib.urlopen(url)
soup = BeautifulSoup(site, "html.parser")

synonymer = soup.find("div", "boxContent")


rank = synonymer.find_all("b")
submeaning = synonymer.find_all("i")
synonym = synonymer.find_all("a")

for s in synonymer:
    if s in rank:
        print("\n%s" % s.get_text(), end='')

    elif s in synonym:
        print(s.get_text(), end='')
        if s.next_sibling in rank:
            print()
        elif s.next_sibling in submeaning:
            pass
        else:
            print(", ", end='')

    elif s in submeaning:
        if s.previous_sibling in rank:
            print("%s: %s" % (s.get_text(), s.next_sibling), end='')
        else:
            print("\n%s: %s" % (s.get_text(), s.next_sibling), end='')
print()
