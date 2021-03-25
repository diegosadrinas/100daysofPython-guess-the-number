import random
from art import logo



#funciones
#funcion para elegir el número:
def random_number():
  number = random.choice(range(101))
  return number


def difficulty(user_input):
  result = 0
  if user_input == 'easy':
    result = 10
  if difficulty_input == 'hard':
    result = 5
  return result

#función para determinar resultado:
def guess_result(guess, number):
  high = "Too high."
  low = "Too low."
  win = f"You got it! The answer was {number}."
  if guess > number:
    return high
  if guess < number:
    return low
  if guess == number:
    return win

#funcion que chequea ganador:
def check_winner(guess, number):
  winner = False
  if guess == number:
    winner = True
  return winner



#strings del juego
welcome_message = "Welcome to the Number Guessing Game!\nI'm thinking in a number between 1 and 100."
lose_message = "You have ran out of guesses. You lose."
guess_again = "Guess again."

#variables fuera del loop
playing = True
print(logo)
print(welcome_message)
number = random_number()
difficulty_input = input("Choose a difficulty. Tyoe 'easy' or 'hard': ").lower()
attempts = difficulty(difficulty_input)  


#ciclo del juego:
print(number)
while playing:
  print(f"You have {attempts} remaining to guess the number.")
  guess_input = int(input('Make a guess: '))
  result = guess_result(guess=guess_input, number=number)
  print(result)
  user_wins = check_winner(guess=guess_input, number=number)
  if user_wins == False:
    attempts -= 1
    if attempts != 0:
      print(guess_again)
  if user_wins:
    playing = False
  if attempts == 0:
    playing = False
    print(lose_message)

  

