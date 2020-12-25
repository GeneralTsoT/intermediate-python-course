import random
def main():
 
 dice_rolls = int(input('How mony dice would you like?'))
 dice_sides = int(input('sO how many sides?'))
 dice_sum = 0
 for i in range(0,dice_rolls):
  roll= random.randint(1,dice_sides)
  dice_sum = dice_sum + roll
  if roll == 1:
   print (f'you rolled a {roll}! Critical fail')
  elif roll == dice_sides:
   print(f'you rolled a {roll}! Critical Success!!')
  else:
   print(f"You rolled a {roll}")
 print(f"you have rolled a total of {dice_sum}")

if __name__== "__main__":
  main()
