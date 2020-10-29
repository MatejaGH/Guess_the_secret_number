# Uporabnik lahko ugiba samo 1x, potem se program zaključi.

secret = 4
guess = int(input("Guess!"))

if guess == secret:
    print("Yes!")
else:
    print("No!")
