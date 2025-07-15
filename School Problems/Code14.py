# Write A Program To Take All The Numbers Which are present in a list but not in the second list:

a=[1,2,3,4,5,6,8,9,0]
b=[1,2,3,4]

for i in a:
  if i not in b:
    print(i)