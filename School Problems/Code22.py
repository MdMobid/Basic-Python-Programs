# SUM FINDER FOR A GIVEN RANGE

#Taking 'sum' as a variable
sum=0

#Input Variables
beg=int(input("Enter From Where To Start: "))
end=int(input("Enter From Where To End: "))

#Loop
for i in range (beg,end+1):
  sum=sum+i
print("The Total Sum",sum)