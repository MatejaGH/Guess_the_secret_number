# Uporabnik lahko ugiba neštetokrat. Program se ustavi, ko uporabnik ugane, ker takrat več ni zadoščeno pogoju (WHILE).
secret = 4
guess = 0

while guess != secret:
    guess = int(input("Guess!"))
if guess == secret:
    print("Yes!")
else:
    print("No!")
