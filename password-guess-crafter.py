#!/usr/bin/python3

import sys

filename = "base-wordlist.txt"
placeholder = "<PERSONAL_INFO>" 
outputFilename = "custom-wordlist.txt" 

def replace_placeholder():
    with open(filename, 'r') as file:
        content = file.read()

    replacement = sys.argv[1]
    content = content.replace(placeholder, replacement)

    with open(outputFilename, 'w') as file:
        file.write(content)

if len(sys.argv) == 1:
	print("Welcome to Sniper! Your best Password Guesser!")
	print("Provide the personal information that you find out about your target and see your forecast")
	print("Usage: python sniper.py <PERSONAL_INFO>")
	sys.exit(1)
else:
	replace_placeholder()


