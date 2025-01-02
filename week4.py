# Pratice Exercises
# Question 1 Week 4

# Reverse string and palindromes checker
palindrome = input("Enter the string to check if it's palindrome or not : ")
palindrome_checker = ''.join(i for i in palindrome if i.isalnum()).lower()
print(palindrome_checker)
left = 0
right = len(palindrome_checker) - 1
is_palindrome = True
while left < right:
       if palindrome_checker[left] != palindrome_checker[right]:
              is_palindrome = False
              break
       left += 1
       right -= 1

if is_palindrome :
       print(f'{palindrome} is Palindrome')
else:
       print(f'{palindrome} is not Palindrome')

import random
word_guess = ["apple","tiger","spain","grape","sushi", "yacht", "chair", "balloon", "dog", "house" ]
print(f'This is a guess game, Take a guess from this list {word_guess}.\n RULE: Please enter only the specific word length and no number or digit')
# Generate a random word from the given list
random_word = random.choice(word_guess)
print(f"Guess the word. The word contains {len(random_word)} letters.")
# Set the number user have to guess
start = 0
number_of_guesses = 5
while start <  number_of_guesses:
       print(f'You have {number_of_guesses - start} guesses left.')
       start += 1
       guess = input("Guess the word: ")
       if guess.isalpha() and len(guess) == len(random_word):
               if guess.lower() == random_word.lower():
                      print("You guessed correctly!")
                      break
               else:
                     print('Incorrect, Try again')

       else:
              print('Please follow the rules !')

       if start == number_of_guesses:
         print(f'Sorry, you ran out of guesses. The correct word was {random_word}')







