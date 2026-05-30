name       = input("What is your name? ")

try:
    age = int(input("What is your age? "))
    birth_year = 2026 -age
    print("Hello " + name + "!")
    print("You were born in " + str(birth_year))
except ValueError:
    print("Error: Age must be a number, not text!")