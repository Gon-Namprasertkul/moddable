from config import *
from getch import getch
from os import system

print(line1+"_____\n"+line2+"_____\n"+line3+"_____\n"+line4+"_____")

print("Press any key to continue...")
getch()
system("clear")
a=input("Enter a color:")
b=input("Enter a color:")
c=input("Enter a taste: ")
d=input("Enter a person: ")

print("\n\n")

print(line1+a+"\n"+line2+b+"\n"+line3+c+"\n"+line4+d)