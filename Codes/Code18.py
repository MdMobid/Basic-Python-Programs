# Write A Program To Check Whether or not a String is Pallidrom:

list2=[]
list1=eval(input(">> "))
list2.extend(list1)
list3=list2[::-1]
print("")

if list2==list3:
  print("Yes, It's A Pallidrom")
else:
  print("No, It's Not A Pallidrom")