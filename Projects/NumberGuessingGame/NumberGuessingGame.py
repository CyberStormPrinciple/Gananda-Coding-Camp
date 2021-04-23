import random

def game_loop():
  guesses = 0
  comp_guess = random.randint(0, 100)
  while True:
    user_guess = int(input('Guess a number 0-100: '))
    guesses += 1
    if user_guess == comp_guess:
      print(f'\nYou Guessed Correctly! in {guesses} guesses')
      break
    elif user_guess > comp_guess:
      print('\nLower\n')
    else:
      print('\nHigher\n')


if __name__ == "__main__":
  game_loop()
