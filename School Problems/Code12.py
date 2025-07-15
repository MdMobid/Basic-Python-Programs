# Write A Program To Replace All Occurences of Even Numbers by Its Immediate Next Next Odd Number:

print("Enter All Numbers You Want in the List with Comma Seperation: ")
print("For Example: 1,2,3,4,5 \n")

list2=[]
list1=eval(input(">> "))
list2.extend(list1)
print("")

for i in range (0,len(list2)):
  if list2[i]%2==0:
    for j in range (i,len(list2)):
      if list2[j]%2==1:
        replace=list2[j]
        break
    list2[i]=replace

print("Your Resultant List:", list2)