"""My second challenge question in COMP110!"""
__author__ = "730768561"

def guess_a_number() -> None: 
    secret : int = 7
    guess : int = int(input("Guess a number: "))

    print(f"Your guess was {guess}") 

    if guess == secret: 
        print("You got it!")
    elif guess < secret: 
        print(f"Your guess was too low! The secret number is {secret}")
    else:
        print(f"Your guess was too high! The secret number is {secret}")

if __name__ == "__main__":
    guess_a_number()
    
