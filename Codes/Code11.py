# Write A Program To Interchange The First Half of the List with the Second Half:

print("Enter All Numbers You Want in the List with Comma Seperation: ")
print("For Example: 1,2,3,4,5 \n")

list2=[]
list1=eval(input(">> "))
list2.extend(list1)
list3=list2[::]
print("")

leng=len(list2)+1
e=(leng//2)
for i in range (0,leng//2):
  t=list2[i]
  list2[i]=list2[e]
  list2[e]=t
  e=e+1

print("Input List:",list3)
print("Interchanged List:",list2)