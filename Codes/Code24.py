# PRIME NUMBER IDENTIFIER

counter=0
num=int(input("Enter A Number To Identify: "))

for i in range (1,int(num/2)):
    if num%i==0:
        counter=counter+1

if counter==1:
        print("Yes,",num,"is a Prime Number")

else:
    print("No,",num,"is not a Prime Number")