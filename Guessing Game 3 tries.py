secret_word = "heraf"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
         guess = input(" Enter Your Guess: ")
         guess_count += 1
    else:
        out_of_guess = True
if out_of_guess:
    print("You lost")
else:
    print(" Yay you won the word was " + secret_word )