import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print('Welcome to Rock, Paper, Scissors!')
select = int(input('Enter 1 for Rock, 2 for Paper, 3 for Scissors '))
num = random.randint(1, 3)

print(f'You chose: {select}')

if select == 1:
    print(rock)
elif select == 2:
    print(paper)
elif select == 3:
    print(scissors)

print(f'Computer chose: {num}')

if num == 1:
    print(rock)
elif num == 2:
    print(paper)
elif num == 3:
    print(scissors)

if num == select:
    print('Draw!')
elif select == 1 and num == 3:
    print('You win!')
elif select == 1 and num == 2:
    print('You lose. Sad face.')
elif select == 2 and num == 1:
    print('You win!')
elif select == 2 and num == 3:
    print('You lose. Sad dog.')
elif select == 3 and num == 1:
    print('You lose. So sad for you.')
elif select == 3 and num == 2:
    print('You win!')
