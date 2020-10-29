# Uporabnik lahko ugiba 3x. Program se ustavi, ko ugane, ker je pri tem pogoju BREAK oziroma po treh poskusih.

secret = 4
attempt = 3

for x in range(attempt):
    print("You have ", attempt-x, " attempts left.")
    guess = int(input("Guess!"))
    if guess == secret:
        print("Yes!")
        break
    else:
        print("No!")
