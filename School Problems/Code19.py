# Write A Program To Count No.of Special Characters Present in a String:

strng=input("Enter Your String Here: ")

a="abcdefghijklmnopqrstuvwxyz"
A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
count=0

for i in strng:
  if i not in a:
    if i not in A:
      if i not in num:
        count=count+1

print("Number of Special Characters:", count)