#!/usr/bin/python3

import sys

filename = "base-wordlist.txt"

namePlaceholder = "<NAME_INFO>" 
petNamePlaceholder = "<PETNAME_INFO>"
birthDatePlaceholder = "<BIRTHDATE_INFO>"

outputFilename = "custom-wordlist.txt" 

print("Welcome to Sniper! Your coolest Password Guesser!")
print("Provide the personal information that you find out about your target and see your forecast")
print("Short usage: python sniper.py <TARGET_NAME> <PETNAME> <BIRTHDATE>")

name = input("Type the name of the target or press enter to set null: ")
petName = input("Type the pet name of the target or press enter to set null: ")
birthDate = input("Type the birthdate of the target or press enter to set null: ")

def replace_placeholder():
    with open(filename, 'r') as file:
        content = file.read()

    content = content.replace(namePlaceholder, name)
    content = content.replace(petNamePlaceholder, petName)
    content = content.replace(birthDatePlaceholder, birthDate)


    with open(outputFilename, 'w') as file:
        file.write(content)

replace_placeholder()


