from random import randint

y=["Rock","Paper","Scissors"]
i=1
while i>0:
  print("We Are Playing Rock, Paper, Scissors")
  print('''
      1 => Rock
      2 => Paper
      3 => Scissors
  ''')

  x=int(input("Enter Your Option: "))
  z=y[randint(0,2)]

  if x==z:
    print("Its a Tie :)")

  if x==0:
    if z==1:
      print("My Paper Covers Your Rock, I won Hurray!")
    if z==2:
      print("Your Rock Broke My Scissor, I lost :(")

  if x==1:
    if z==0:
      print("Your Paper Covers My Rock, You Won")
    if z==2:
      print("My Scissor Cuts Your Paper, Better luck Next Time!")

  if x==2:
    if z==0:
      print("My Rock Broke Your Scissor, As Stronger is me:")
    if z==1:
      print("My Paper was Cut down by your Scissor :(")

'''  h=input("Do you want to Continue? y/n: ")
  if h=="y" or h=="Y":
    from google.colab import output
    output.clear()
    continue

  if h=="n" or h=="N":
    break

print("Thank Your For Playing with Me, Hope to See You Again :)")'''