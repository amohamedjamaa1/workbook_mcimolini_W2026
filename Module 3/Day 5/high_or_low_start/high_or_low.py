import random

# Generate a random integer between a range (1-100)
random_number = random.randint(1, 100)

user_input = input("Please guess a number (1-100): ")
user_guess = int(user_input)

high_low_input = input("Do you think your # is higher or lower? (h/l) ")

print(f"User Guess: {user_guess}")

print(f"The random number is: {random_number}")

result = ""

if user_guess == random_number:
    result = "correct"
elif user_guess > random_number:
    result = "high"
elif user_guess < random_number:
    result = "low"
else:
    result = "unknown"

if result == "correct":
    print("You guessed correctly! Lucky you!")
elif result == "high" and high_low_input == "h":
    print("You're right! Your number was too high!")
elif result == "low" and high_low_input == "l":
    print("You're right! Your number was too low!")
else:
    print("This game is too hard! Please try again!")