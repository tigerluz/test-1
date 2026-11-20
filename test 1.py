secret = 27
attempts = 5

while attempts > 0:
    guess = int(input("Enter your guess (1-50): "))

    if guess == secret:
        print("You win! You guessed the secret number.")
        break

    difference = abs(secret - guess)

    if difference >= 20:
        print("Ice cold")
    elif difference >= 10:
        print("Cold")
    elif difference >= 5:
        print("Warm")
    else:
        print("Hot")

    attempts -= 1

    print("Lives remaining:", end=" ")
    for i in range(attempts):
        print("♥", end=" ")
    print()

if attempts == 0:
    print("Game Over!")
    print("The secret number was:", secret)