# Write a Python program to take a string input from the user, count and print the number of small letters, capital letters, and digits in a given string.

str=input()
a="abcdefghijklmnopqrstuvwxyz"
A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="1234567890"
scnt=0
capcnt=0
numcnt=0

for i in str:
  if i in a:
    scnt=scnt+1
  elif i in A:
    capcnt=capcnt+1
  elif i in num:
    numcnt=numcnt+1

print("Small Letters:", scnt)
print("Capital Letters:", capcnt)
print("Digis:", numcnt)