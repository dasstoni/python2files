

import urllib, re, lib2to3

#this function handles opening and reading web pages
def open_page(page):
    try:
        web_page = urllib.urlopen(page)
        lines = web_page.read()
        if "404 Not Found" in lines:
            print "That page doesn't exist on the server."
        web_page.close()
    except:
        print "Error opening that URL!"
        lines = []
    return lines

def caesar(letter, key):
    """ letter is a single text character, and key is an integer"""
    alpha = "abcdefghijklmnopqrstuvwxyz"

    #Newlines and other punctuation should be ignored
    if letter not in alpha:
        return letter
    #Otherwise we return the letter caesar ciphered by the key
    else:
        new_index = (alpha.index(letter) + key) % 26
        return alpha[new_index]


#main
start = "http://www.soic.indiana.edu/faculty-research/directory/index.html"
print "Parsing:", start
if open_page(start):
    print "Page loaded successfully."

matches = re.findall("profile_id=[\d]+'[>][\w.&#; -]+", open_page(start))
print "There are", len(matches), "names."
names = [" ".join([piece for piece in entry.split(">")[1].split(" ") if piece]) for entry in matches]

matches = re.findall('znvygb:[\w@.]*', open_page(start))
print "There are", len(matches), "emails."
emails = ["".join([caesar(letter, 13) for letter in entry.split(':')[1]]) for entry in matches]

matches = re.findall('<br />[(]?[\d]{0,3}[)]?[ ]?[\d]{0,3}-?[\d]{0,5}<br />', open_page(start))
print "There are", len(matches), "phone numbers."
numbers = [entry.replace("<br />","") for entry in matches]

print "All faculty data loaded."

target = raw_input("\nSearch for what name? ")

for i in range(len(names)):
    if target.lower() in names[i].lower():
        print names[i], " " * (25 - len(names[i])), emails[i], " " * (35 - len(emails[i])), numbers[i]
