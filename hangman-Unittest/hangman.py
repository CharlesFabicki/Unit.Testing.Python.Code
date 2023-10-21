import random


class Hangman:
    def __init__(self, words, max_attempts=5):
        self.words = words
        self.max_attempts = max_attempts
        self.word = ""
        self.hidden_word = []
        self.attempts = 0
        self.hangman_stages = [
            """
               --------
               |      |
               |      O
               |
               |
               |
            """,
            """
               --------
               |      |
               |      O
               |      |
               |
               |
            """,
            """
               --------
               |      |
               |      O
               |     /|
               |
               |
            """,
            """
               --------
               |      |
               |      O
               |     /|\\
               |
               |
            """,
            """
               --------
               |      |
               |      O
               |     /|\\
               |     /
               |
            """
        ]

    def choose_word(self):
        self.word = random.choice(self.words)
        self.hidden_word = ["_" for _ in self.word]

    def display_hidden_word(self):
        return " ".join(self.hidden_word)

    def guess_letter(self, letter):
        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.hidden_word[i] = letter
        else:
            self.attempts += 1

    def is_game_over(self):
        if "_" not in self.hidden_word or self.attempts >= self.max_attempts:
            return True
        return False

    def play(self):
        self.choose_word()
        print("Welcome to Hangman!")
        print("Guess the hidden word. You have", self.max_attempts, "chances.")
        print(self.display_hidden_word())

        while not self.is_game_over():
            letter = input("Enter a letter: ").lower()
            if len(letter) != 1 or not letter.isalpha():
                print("Please enter a single letter.")
                continue

            self.guess_letter(letter)
            print(self.display_hidden_word())

            if self.attempts < self.max_attempts:
                print(self.hangman_stages[self.attempts])

            if "_" not in self.hidden_word:
                print("Congratulations, you guessed the word:", self.word)
                break  # Add this break statement to exit the loop upon winning

        if "_" in self.hidden_word:
            print("""
               --------
               |      |
               |      O
               |     /|\\
               |     / \\
               |
            """
                  "Sorry, you couldn't guess the word. It was:", self.word)


def play_hangman():
    words_to_guess = ["python", "programming", "computer", "games", "book", "coding"]

    while True:
        hangman_game = Hangman(words_to_guess)
        hangman_game.play()

        play_again = input("            Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break


if __name__ == "__main__":
    play_hangman()
