import random

# Dictionary to map user input to moves
dict = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissor'
}

userPoints = 0
compPoints = 0
game = 0
while game <= 10:
    game += 1
    # Take input from the user
    user = input(f'Type r for rock, p for paper, s for scissors OR x for exit: ')
    print()

    # Check if the user wants to exit
    if user == 'x':
        break

    # Check if the user input is valid
    if user not in dict:
        print('Enter a valid key')
        continue

    # Generate computer's choice
    comp = random.choice(['rock', 'paper', 'scissor'])
    userMove = dict[user]

    print(f'You chose: {userMove}, Computer chose: {comp}')

    # If both moves are the same, it's a tie
    if userMove == comp:
        print("It's a tie!")
        continue

    # Check winning conditions for the user
    if (userMove == 'rock' and comp == 'scissor') or \
       (userMove == 'paper' and comp == 'rock') or \
       (userMove == 'scissor' and comp == 'paper'):
        userPoints += 1
        print("You win this round!")
    else:
        compPoints += 1
        print("Computer wins this round!")

    print(f'User points: {userPoints}, Computer points: {compPoints}')
    print()

# Final result
if userPoints > compPoints:
    print("You win the game!")
elif userPoints < compPoints:
    print('Computer wins the game!')
else:
    print("It's a tie game!")
