# Write A Program To Display All Prime Numbers Between A Given Range

beg=int(input("Enter a Number From Where To Start: "))
end=int(input("Enter a Number From Where To End: "))

print("The Prime Numbers Between The Above Range Are As Follows: ")

for i in range (beg,end+1):
    if i>1:
        for j in range (2,i):
            if i%j==0:
                break
        else:
            print(i)