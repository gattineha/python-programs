import random

print('Welcome to the game "Guess the number" ')
print('Let me think of a number between 1 and 100.')
level = input('Choose the level of difficulty... Type "easy" or "hard":').lower()
if level == 'easy':
    print('The number is between 1 to 50')
    numbers = random.randint(1, 50)
    chances = 10
elif level == 'hard':
    print('The number is between 1 to 100')
    numbers = random.randint(1, 100)
    chances = 5

while chances > 0:
    print(f'You have {chances} chances to guess the number')
    guess = int(input('Enter number to guess:'))
    if guess == numbers:
        print(f'Your guess is correct ! The number is {guess}.')
        print('Thank you for playing !')
        break
    elif guess > numbers:
        print('Your guess is too large.')
    else:
        print('Your guess is too small')
    chances -= 1
    if chances == 0:
        print(f'You are out of chances. And the number was {numbers}')
        print('Thank you for playing !')
    
