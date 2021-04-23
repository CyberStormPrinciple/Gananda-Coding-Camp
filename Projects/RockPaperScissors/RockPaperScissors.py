import random
""" Rock Paper Scissors game """

# This project covers...

# Function syntax and use
# Single Responsibility Principle
# while loop and break
# User input
# if, else, elif statements
# String concatenation and lower() function
# Random
# Dictionaries
# Printing to system
# Comments
# Python operators( =, ==, +=, and, or, + )
# Boolean 
# Casting

def main():
    """ Main game loop for Rock Paper Scissors """
    users_wins = 0
    computers_wins = 0
    # Infinite loop until broken by break case
    while True:
        print("# of Users wins: " + str(users_wins))
        print("# of Computers wins: " + str(computers_wins))
        print('------------------------')
        users_answer = users_move()
        # Break case to exit loop
        if users_answer == 'q':
            break
        print('========================')
        print('The user went for ' + users_answer)
        computers_answer = computers_move()
        print('The computer went for ' + computers_answer)
        result = determine_winner(users_answer, computers_answer)
        print()
        if (result == 'user'):
            users_wins += 1
            print('You won')
        elif (result == 'computer'):
            computers_wins += 1
            print('The computer won')
        else:
            print('You both tied')
        print('------------------------')


def users_move():
    """ Asks the user for their move """
    user_move = input("""
Type... 
    r for Rock  | s for Scissors,
    p for Paper | q to end game
: """)
    return check_move(user_move)


def check_move(user_move):
    """Checks for valid user input"""
    # Changes the inputed string to all lower case
    user_move = user_move.lower()
    # Valid input check
    if user_move == 'q':
        return 'q'
    elif user_move == 'r' or user_move == 'p' or user_move == 's':
        # Holds a key value pair relating the letter to the full move name
        moves = {
            'r': 'Rock',
            'p': 'Paper',
            's': 'Scissors'
        }
        return moves[user_move]
    else:
        print("Please enter a valid choice")
        return users_move()


def computers_move():
    """ Returns computers random move """
    return random.choice(['Rock', 'Paper', 'Scissors'])


def determine_winner(users_answer, computers_answer):
    """ Determines who is the winner based off of the rules of Rock Paper Scissors """
    # Rules
    # Rock == Rock: tie same for other moves
    # Rock > Scissors
    # Paper > Rock
    # Scissors > Paper
    result = ""

    if users_answer == computers_answer:
        result = 'tie'
    elif users_answer == 'Rock' and computers_answer == 'Scissors':
        result = 'user'
    elif users_answer == 'Paper' and computers_answer == 'Rock':
        result = 'user'
    elif users_answer == 'Scissors' and computers_answer == 'Paper':
        result = 'user'
    elif users_answer == 'Scissors' and computers_answer == 'Rock':
        result = 'computer'
    elif users_answer == 'Rock' and computers_answer == 'Paper':
        result = 'computer'
    elif users_answer == 'Paper' and computers_answer == 'Scissors':
        result = 'computer'
    return result
    
if __name__ == "__main__":
    main()
