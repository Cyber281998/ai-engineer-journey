def greet_user(name, age):
    birth_year = 2026 - age
    print("Hello " + name + "!")
    print("You were born in " + str(birth_year))

def get_user_input():
    name = input("What is your name? ")
    try:
        age = int(input("What is your age? "))
        return name, age
    except ValueError:
        print("Error: Age must be a number ")
        return None, None
    
name, age = get_user_input()

if name is not None:
    greet_user(name, age)
    