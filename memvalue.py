# import file
from sys import argv
script, filename = argv
txt = open(filename)

# read the entire file into a string variable
contents = txt.read() 
#split file into individual words
values=contents.split()

#Get word number from user (ex. 1000th word after starting address)
wordval = input("nth word after starting address? ")
#Add two to the word value to account for the first line (ex. "Memory address: 0x80010000")
wordnum = wordval + 2

word = values[wordnum]

print ("%s") %word


    