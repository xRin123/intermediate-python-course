import random
def main():
  dice_rolls = int ( input ( '你想掷多少个骰子？' ))
  dice_size = int(input('骰子有几面？'))
  dice_sum = 0
  for i in range(0, dice_rolls):
    roll = random.randint(1, dice_size)
    dice_sum += roll
    if roll == 1:
      print(f'You roll a {roll} !Critical Fail')
    elif roll == dice_size :
      print(f'You roll a {roll}！关键的成功！')
    else:
      print(f'You roll a {roll} ')
  print(f'你总共掷了{dice_sum} ')

if __name__== "__main__":
  main()