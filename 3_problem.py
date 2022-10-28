# Write a program to check if two strings are a rotation of each other?


def checkRotation(str1, str2): 
    temp = '' 
  
    # Check if lengths of two strings are equal or not 
    if len(str1) != len(str2): 
        return False
  
    # storing concatenated string 
    temp = str1 + str1 
  
    
    if str2 in temp: 
        return True #returning true if 2nd string is present in concatenated string
    else: 
        return False

str1 = input("enter the string : ")
str2 = input("enter the second string : ")

if checkRotation(str1, str2): 
    print("Given Strings are rotations of each other.")
else: 
    print("Given Strings are not rotations of each other.")