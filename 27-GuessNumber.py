n = 90
allowed_guess = 5
guess_count = 0


while (guess_count < allowed_guess):
    guess_count += 1
    guess = int(input("Enter number: "))
    if guess < n:
        print("You guessed wrong, go higher!")
    elif guess > n:
        print("You guessed wrong, go lower!")
    else:
        print("You won! you took", guess_count, "total guesses")
        break
    

if (guess_count == allowed_guess):
    print("You lose, 5 chances expired")
    

