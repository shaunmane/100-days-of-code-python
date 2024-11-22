import random

rock = r'''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        '''
paper = r'''
            _______
        ---'   ____)____
                  ______)
                  _______)
                _______)
        ---.__________)
        '''
scissors = r'''
            _________
        ---'     ____)____
                    ______)
                 __________)
                (____)
        ---.__(___)
        '''

game = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer = random.randint(0, 2)

if player == computer:
    print(game[player])
    print(f"Computer chose: {game[computer]}")
    print("It's a draw")    

elif player == 0:
    print(rock)
    if computer == 1:
        print(f"Computer chose: {paper}")
        print("You lose!")
    elif computer == 2:
        print(f"Computer chose: {scissors}")
        print("You win!")

elif player == 1:
    print(paper)
    if computer == 0:
        print(f"Computer chose: {rock}")
        print("You win!")
    elif computer == 2:
        print(f"Computer chose: {scissors}")
        print("You lose!")

elif player == 2:
    print(scissors)
    if computer == 0:
        print(f"Computer chose: {rock}")
        print("You lose!")
    elif computer == 1:
        print(f"Computer chose: {paper}")
        print("You win!")

else:
    print("Invalid input, you lose!")