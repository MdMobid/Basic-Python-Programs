# Write a program which accepts a number from the user and prints the frequency of the number in the list LST, if number is not in the LST it should print “Number not available"

LST=[1,2,3,4,5,5,5,6,6,7,7,8,8,8,1,1,1,4,9]
count=0

num=int(input("Enter A Number: "))
for i in range (0,len(LST)):
  if LST[i]==num:
    count=count+1

if count==0:
  print("Number Not Available")
else:
  print("Frequency of", num, "is:", count)
