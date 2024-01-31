#David Stonikas

import urllib, re, webbrowser

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





#main

base = "http://www.soic.indiana.edu/undergraduate/courses/index.html"

print "Parsing:", base

computer_science = [course for course in re.findall('CSCI [A-Z][\d]+ [\w]+[-]?[ ]?[\w]*[ ]?[\w]*[ ]?[\w]*[ ]?[\w]*[,]?[\w]*[ ]?[\w]*[ ]?[\w]*',open_page(base))]

print "CSCI Undergraduate Courses:"
for course in computer_science:
    print course

informatics = [course for course in re.findall('INFO [A-Z][\d]+ [\w]+[/]?[,]?[ ]?[&]?[\w]*[,]?[ ]?[\w]*[ ]?[&]?[ ]?[\w]*[ ]?[&]?[\w]*[,]?[\w]*[,]?[ ]?[&]?[\w]*[,]?[ ]?[\w]*[,]?[ ]?[\w]*',open_page(base))]

print "\nINFO Undergraduate Courses:"
for course in informatics:
    print course


search = raw_input("\nPlease enter a word to search for:")

##search_results1 = [course for course in range(len(computer_science))if search.lower() in computer_science[course].lower()]


for course in range(len(computer_science)):
    if search.lower() in computer_science[course].lower():
        print computer_science[course]

for course in range(len(computer_science)):
    if search.lower() in computer_science[course].lower():
        print informatics[course]
    

choice = raw_input("Enter the name of a course (Ex: I210) to view it, or press ENTER: ")

for course in range(len(computer_science)):
    if choice.lower() in computer_science[course].lower():
        webbrowser.open(base+"?number="+choice+"&department=CSCI")

for course in range(len(informatics)):
    if choice.lower() in informatics[course].lower():
        webbrowser.open(base+"?number="+choice+"&department=INFO")



