import random

def main():

  #dice_rolls = 2
  dice_sum = 0

  dice_rolls = int(input('How many dice would you like to rool? '))
  dice_size = int(input('How many sides are in the dice? '))

  for i in (0, dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum += roll
    if roll == 1:
      print(f'You rolled a {roll}! Critical Fail')
    elif roll == dice_size:
      print(f'You rolled a {roll}! Critical Success!')
    else:
      print(f'You rooled a {roll}')

  print(f'You rolled a total of {dice_sum}')

if __name__== "__main__":
  main()