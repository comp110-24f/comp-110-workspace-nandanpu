"""This program allows the user to play a fun game of Wordle."""
__author__ = "730768561"

def input_guess(word_len : int) -> str: 
    input_guess : str = input(f"Enter a {word_len} character word: ")

    while len(input_guess) != word_len: 
        input_guess = input(f"That wasn't {word_len} chars! Try again: ")
    
    return input_guess

def contains_char(word : str, char : str) -> bool: 
    """This function checks whether a character is located in a word."""
    assert len(char) == 1 # I forgot to include this piece of code and the function ran even when char has a length greater than 1. 
    word_index : int = 0
    while word_index < len(word): 
        if word[word_index] == char: 
            return True
        word_index += 1
    return False 

def emojified(guess : str, secret_word : str) -> str: 
    """This function compares the two strings and will spit out a group of emojis based on the result."""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_string : str = "" # Intializing this as an empty string was important since I was able to add to it as the while loop processed.

    i : int = 0
    while i < len(guess): # At first, I tried using a nested while loop to check every single case. But, I soon found out I was overthinking the entire process and I just needed to use one while loop and some conditional statements.
        if guess[i] == secret_word[i]: 
            emoji_string += GREEN_BOX
        elif (contains_char(word = secret_word, char = guess[i])): 
            emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX

        i += 1
    return emoji_string

def main(secret : str) -> None: 
    """This is the main game function that ties all the functions together."""
    
    curr_turn : int = 1
    while curr_turn <= 6:
        print(f"=== Turn {curr_turn}/6 ===")
        guess : str = input_guess(len(secret)) # In the beginning, I used used 5 as the argument, but then I realized I need to use the length of the secret word parameter.
        print(emojified(guess = guess, secret_word = secret))

        if secret == guess:
            print(f"You won in {curr_turn}/6 turns!")
            curr_turn = 7 # This is a trick to immediately end the while loop after the user guesses the word.
        elif curr_turn != 6:
            curr_turn += 1
        else:
            print("X/6 - Sorry, try again tomorrow!")
            curr_turn += 1


if __name__ == "__main__": 
    main(secret = "codes")
