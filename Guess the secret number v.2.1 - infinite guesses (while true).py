# Uporabnik lahko ugiba neštetokrat. Program se ustavi, ko ugane, ker je pri tem pogoju BREAK.

secret = 4

while True:
    guess = int(input("Guess!"))
    if guess == secret:
        print("Yes!")
        break
    else:
        print("No!")
