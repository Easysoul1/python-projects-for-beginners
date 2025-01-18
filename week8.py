# Pratice Exercises
# Question 1 Week 8
# Factorial calculation using recursive function
def factorial(number):
       if number == 0 or number == 1:
              return 1
       elif number < 0:
              return "Enter a valid input greater than 1 !"
       else:
              return number * factorial(number - 1)

print(factorial(5))
print(factorial(-5))
print(factorial(1))

# Question 2
# Function calls using decorator
def main(func):
       def wrapper(*args, **kwargs):
              result = func(*args, **kwargs)
              print(f'The result is : {result}')
              return result
       return wrapper

@main
def add(a, b):
       return a + b

add(5, 7)

# Question 3
# Algorithm for Tower of Hanoi 
def tower_of_hanoi(n, source, destination, aux):
       def hanoi (n, from_rod, to_rod, aux_rod):
              if n == 0:
                     return
              hanoi(n-1, from_rod, aux_rod, to_rod)       
              moves.append((n, from_rod, to_rod))
              hanoi(n-1, aux_rod, to_rod, from_rod)
       moves = []
       hanoi(n, source, destination, aux)
       for move in moves :
              print(f'Move disk {move[0]} from {move[1]} to {move[2]}')

n = 3
tower_of_hanoi(3, 'A', 'C', 'B')
       
