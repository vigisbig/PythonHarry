def lets_play():
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
    play_again()
    
def play_again():
    wanna_play = input("Want to play again 'Y' or 'N': ")
    if (wanna_play.upper() == "Y"):
        lets_play()
    else:
        exit
lets_play()
