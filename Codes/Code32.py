# Write a Python program that initializes a variable temp to 500 and then subtracts all the values in the dictionary from temp using a loop. Finally, print the result.

Dict= { 'A' : 10, 'B' : 20, 'C' : 100 , 'D' :200} # Given dictionary

temp=500;
for value in Dict.values( ):
  temp-= value
print("Final",temp)