# Write A Program To Display All The Prime And Composite Number Present in a List:

print("Enter All Numbers You Want in the List with Comma Seperation: ")
print("For Example: 1,2,3,4,5 \n")

list2=[]
list1=eval(input(">> "))
list2.extend(list1)
print("")

prime=[]
nprime=[]

for numi in list2:
  if numi==0:
    nprime.append(0)
  elif numi==1:
    nprime.append(1)
  else:
    break

for numi in list2:
  if numi==0 or numi==1:
    continue

  for i in range(2,numi//2 +1):
    if numi % i == 0 :
      nprime.append(numi)
      break
      
  else:
    prime.append(numi)

print("Prime List:", prime)
print("Composite List:", nprime)