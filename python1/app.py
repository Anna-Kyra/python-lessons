secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses): # Als de user die secret word niet heeft geraden gaat het nog een keer door de function
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses: #Je hoeft geen === True op te schrijven, hij is standaard true
    print("You lose!!")
else:
    print("You win!")