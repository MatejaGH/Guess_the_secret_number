# Uporabnik lahko ugiba neštetokrat. Program se ustavi, ko ugane, ker je pri tem pogoju BREAK.
# Dodatno program ob vsakem ugibanju uporabnika usmeri k pravi rešitvi.

secret = 4
attempts = 0

while True:
    guess = int(input("Guess!"))
    attempts += 1

    if guess == secret:
        print("Yes!")
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Try something smaller.")
    elif guess < secret:
        print("Try something bigger.")
