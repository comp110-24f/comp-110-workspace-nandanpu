"""A fun Chardle program needed for the Wordle project later."""

__author__ : str = "730768561"

def input_word() -> str: 
    input_word : str = input("Enter a 5 character word: ")

    if(len(input_word) == 5): 
        return input_word
    else:
        print("Error: Word must contain 5 characters.")
        exit() # Rather than replacing the return statement, I first tried to put the exit under the return, but it didn't run since the return would've already ended the function before geting to the exit.

def input_letter() -> str: 
    input_letter : str = input("Enter a single character: ")

    if(len(input_letter) == 1):
        return input_letter
    else:
        print("Error: Character must be a single character.")
        exit()

def contains_char(word: str, letter: str) -> None: 
    print(f"Searching for {letter} in {word}")
    count : int = 0

    # While creating this code, I realized that a while loop or a for loop would be much more efficient than to tediously type out everything single if-statement.
    if(word[0] == letter): 
        print(f"{letter} found at index 0")
        count += 1
    
    if(word[1] == letter): 
        print(f"{letter} found at index 1")
        count += 1
    
    if(word[2] == letter): 
        print(f"{letter} found at index 2")
        count += 1
    
    if(word[3] == letter): 
        print(f"{letter} found at index 3")
        count += 1
    
    if(word[4] == letter): 
        print(f"{letter} found at index 4")
        count += 1

    if(count == 0): 
        print(f"No instances of {letter} found in {word}")
    else: 
        print(f"{count} instances of {letter} found in {word}")

def main() -> None:
    contains_char(word = input_word(), letter = input_letter())

if __name__ == "__main__": 
    main()