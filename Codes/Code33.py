# Write a Python program using a for loop that iterates through numbers from 15 to 30 (exclusive) in steps of 5. If any number in the loop is divisible by 20, the loop should stop immediately using break. Otherwise, it should print the number.

for a in range (15,30,5) :
  if a%20==0:
    break
  print(a)