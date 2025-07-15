# LCM AND HCF FINDER OF TWO NUMBERS

first=int(input("Enter Your First Number: "))
second=int(input("Enter Your Second Number: "))

if first>second:
  smaller=second
else:
  smaller=first

for i in range (1,smaller+1):
  if ((first%i==0) and (second%i==0)):
    HCF=i
LCM=(first*second)/HCF

print("The HCF of", first, "and", second, "number is", int(HCF))

print("The LCM of", first, "and", second, "number is", int(LCM))