# Write A Program To Take Input For a Name And Display Output in the Given Format:
# Input(Name) = Md Mobid Hossain
# Output = M.M. Hossain

name=input("Enter Your Name: ")
name=name.split(" ")
short=""

for i in range (0,len(name)):
  if i<len(name)-1:
    a=name[i]
    b=a[0]
    short=short+b+"."

  if i==len(name)-1:
    short=short+" "+name[i]

print(short)
