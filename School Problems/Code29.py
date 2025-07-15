# Write a Python program to print all the vowels present in a given string one by one.

string="Hello There I am Mobid" # Given string
vowels="AEIOUaeiou"
for i in string:
  if i in vowels:
    print(i)