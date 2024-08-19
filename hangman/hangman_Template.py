import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        # Initialize the attributes
        gen_number = random.randint(0, len(word_list) - 1)
        self.word = list(word_list[gen_number])
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))  # Unique letters
        self.num_lives = num_lives
        self.list_letters = []

        # Print two messages upon initialization
        print(f"The mistery word has {len(self.word)} characters")
        print(self.word_guessed)

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked
        '''
        letter = letter.lower()
        if letter in self.word:
            # Replace '_' in word_guessed with the correct letter
            for index, char in enumerate(self.word):
                if char == letter:
                    self.word_guessed[index] = letter
        else:
            # Reduce the number of lives if the letter is not in the word
            self.num_lives -= 1

        # Update the number of UNIQUE letters remaining
        self.num_letters = len(set(self.word) - set(self.word_guessed))
        # Print the updated word_guessed and remaining lives
        print(self.word_guessed)
        print(f"Lives remaining: {self.num_lives}")

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single alphabetic character
        If it passes both checks, it calls the check_letter method.
        '''
        while True:
            # Assign the letter to a variable called `letter`
            letter = input("Please enter a letter: ").strip().lower()

            # Check if the letter is a single alphabetic character
            if len(letter) != 1 or not letter.isalpha():
                print("Please, enter a single alphabetic character.")
                continue

            # Check if the letter has already been tried
            if letter in self.list_letters:
                print(f"{letter} was already tried.")
            else:
                # Add the letter to the list of tried letters and check it
                self.list_letters.append(letter)
                self.check_letter(letter)
                break

def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)

    # Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    while game.num_lives > 0 and game.num_letters > 0:
        game.ask_letter()
    
    # Check the outcome of the game
    if game.num_letters == 0:
        print("Congratulations! You won!")
    else:
        print(f"You lost! The word was {''.join(game.word)}")

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
