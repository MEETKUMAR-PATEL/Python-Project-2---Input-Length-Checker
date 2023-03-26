# Use this file to code your solution for Task 3 in Achievements.
# Name:                 InputLengthChecker.py
# Author:               Meetkumar Patel
# Date Created:         January 25, 2022
# Date Last Modified:   January 30, 2022 

# Purpose:
#
#This program will check the users contry name by the length function 
#first user will be propmpt to enter the country 
#if the user enters a letter only prompt to redo
#if the user enter a contry name more than 20 that is more than 21 chars redo again
#then keep this looping until user doesnot give the write input:


while True:
    print("\nWelcome Users!!!\n")

    #propmt user input for the country name.
    country = len(input("Please Enter a Name of Country:\n").strip(" "))
# here it checks if the length of the 
    if country <= 1:
        print("Sorry.Country name must be longer than one letter.")
    elif country >= 21:
        print("Sorry.Country name cannot be more than 20 letters in length.")
    else:
        print("Thank you!!\n")
        break

