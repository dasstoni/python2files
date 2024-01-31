print "Caesar Encryption"


word= raw_input("Please enter a word:")
number= int(raw_input("Please enter a number for the key:"))

letter_tuple=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",
              "u","v","w","x","y","z")
range=(26)
for letter_tuple in range(26)+ number:
    print word
