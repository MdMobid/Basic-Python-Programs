# Write A Program To Count No.of Vowels and Consonants Present in a String:

strng=input("Enter Your String Here: ")
vowels="aeiouAEIOU"
c=0
d=0

for i in strng:
  if i in vowels:
    c=c+1
  if i not in vowels:
    d=d+1

print("No.of Vowels: ", c)
print("No.of Consonants:", d)