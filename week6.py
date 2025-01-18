# Pratice Exercises
# Question 1 Week 6
# Prime number checker
# A prime number is a number that is only divisible by 1 and itself. For example, 2, 3, 5, 7, 11, 13, 17, etc. 
import math
range_check = int(input('Enter the maximun number for the prime check: '))
for i in range(2, range_check):
              is_primeNumber = True
              for j in range(2, int(math.sqrt(i))+1):
                     if i % j == 0:
                            is_primeNumber = False
                            break
              else:
                     print(f'{i} is a prime number')


# Question 2
# Multiplication Table
print('This is mulyiplication table 1 - 12')
for i in range(1, 13):
       for j in range(1, 13):
              print(f'{i} * {j} = {i * j}\n')


# Question 3
# Number guess game
import random
guess_limit = 10
random_number = random.randint(1, 30)
for i in range(guess_limit + 1):
       print(f'You have {guess_limit} guesses left')
       guess = int(input('Enter the guess number from 1 to 30: '))
       if guess == random_number:
              print('You Won !')
              break
       else:
              print('Try again !')
              guess_limit -= 1
              if guess > random_number:
                     print(f'{guess} too high, try reducing it')
              elif guess < random_number :
                     print(f'{guess} too low, try increasing it')












