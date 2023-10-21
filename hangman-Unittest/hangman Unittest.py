import unittest
from hangman import Hangman


class HangmanTest(unittest.TestCase):
    def test_choose_word(self):
        words_to_guess = ["python", "programming", "computer", "games", "book", "coding"]
        hangman_game = Hangman(words_to_guess)
        hangman_game.choose_word()
        self.assertIn(hangman_game.word, words_to_guess)

    def test_guess_letter_correct(self):
        words_to_guess = ["python"]
        hangman_game = Hangman(words_to_guess)
        hangman_game.word = "python"
        hangman_game.hidden_word = ["_", "_", "_", "_", "_", "_"]
        hangman_game.guess_letter("p")
        self.assertEqual(hangman_game.hidden_word, ["p", "_", "_", "_", "_", "_"])

    def test_guess_letter_incorrect(self):
        words_to_guess = ["python"]
        hangman_game = Hangman(words_to_guess)
        hangman_game.word = "python"
        hangman_game.hidden_word = ["_", "_", "_", "_", "_", "_"]
        hangman_game.guess_letter("z")
        self.assertEqual(hangman_game.attempts, 1)

    def test_is_game_over_false(self):
        words_to_guess = ["python"]
        hangman_game = Hangman(words_to_guess)
        hangman_game.choose_word()
        hangman_game.guess_letter("a")
        self.assertFalse(hangman_game.is_game_over())

    def test_is_game_over_true(self):
        words_to_guess = ["python"]
        hangman_game = Hangman(words_to_guess)
        hangman_game.hidden_word = ["p", "y", "t", "h", "o", "n"]
        hangman_game.attempts = 5
        self.assertTrue(hangman_game.is_game_over())


if __name__ == "__main__":
    unittest.main()
