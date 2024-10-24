import random
name1 = input("Type your name: ")
print(f"hello my name is {name1}")
print("guess a number between 1-10")
guess = int(input("enter your guess: "))
number_to_guess = random.randint(1, 10)
if guess == number_to_guess:
    print("good job you guessed the number, oh wait DIDDY IS COMING RUN")
elif guess > number_to_guess:
    print(f"Your high, erm it was actually {number_to_guess}")
else:
    print(f"get high, erm it was actually {number_to_guess}")