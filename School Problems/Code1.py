# Write A Program To Take Input Of A Four Digit And Display Its String Equivalent:

number=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
nty=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninty"]
tens=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]

n=input("Enter a Number: ")
if len(n)>4:
  print("Can't Proceed For More Than 4 Digit Number")
else:
  a=[]
  for i in range (0,len(n)):
    a.append(int(n[i]))

  num=""
  if a[0]!=0:
    num=num+number[a[0]] + " Thousand "

  if a[1]!=0:
    num=num+number[a[1]] + " Hundred "

  if a[2]!=0:
    if a[2]==1:
      num=num+tens[a[3]]
    else:
      num=num+nty[a[2]]

  else:
    if a[0]!=0:
      num=num+number[a[3]]

  print(num)
