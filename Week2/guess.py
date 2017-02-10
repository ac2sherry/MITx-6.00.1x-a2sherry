guess_min = 0
guess_max = 100
while True:
    guess = (guess_max + guess_min) // 2
    print('Is your secret number ',guess,'?')
    print("Enter 'h' to indicate the guess is too high. \
        Enter 'l' to indicate the guess is too low. \
        Enter 'c' to indicate I guessed correctly. ")
    char = input()
    if char == 'h':
        guess_max = guess
    elif char == 'l':
        guess_min = guess
    elif char == 'c':
        secret = guess
        break
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was: ",secret)

