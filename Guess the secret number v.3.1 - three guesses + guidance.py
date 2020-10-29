# Uporabnik lahko ugiba 3x. Program se ustavi, ko ugane, ker je pri tem pogoju BREAK oz. po treh poskusih.
# Dodatno program ob vsakem ugibanju uporabnika usmeri k pravi rešitvi.

secret = 4
attempt = 3

for x in range(attempt):
    print("You have ", attempt-x, " attempts left.")
    guess = int(input("Guess!"))
    if guess == secret:
        print("Yes!")
        break
    elif guess > secret:
        print("Try something smaller.")
    elif guess < secret:
        print("Try something bigger.")
