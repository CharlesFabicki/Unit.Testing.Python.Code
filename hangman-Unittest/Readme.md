# Hangman Game Test Suite

This repository contains a test suite for a Hangman game implemented in Python. The test suite utilizes the `unittest` library to evaluate various aspects of the Hangman game, ensuring that it behaves as expected.

## Prerequisites

Before running the test suite, make sure you have Python installed on your system. This test suite is written in Python 3.

## Getting Started

To run the Hangman game test suite, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the repository's directory.
3. Run the test suite.

```
python hangman Unittest.py
```
This command will execute all the test cases defined in the hangman Unittest.py script.

## Test Cases
The test suite contains the following test cases:

1. test_choose_word: Checks if the choose_word method selects a word from the provided list of words.

2. test_guess_letter_correct: Verifies that the game correctly reveals the guessed letter in the hidden word if the guess is correct.

3. test_guess_letter_incorrect: Tests if the game registers an incorrect guess and increments the number of attempts.

4. test_is_game_over_false: Validates that the game is not over when there are attempts remaining.

5. test_is_game_over_true: Verifies that the game is over when there are no attempts remaining, indicating a loss.

## Contributing
Feel free to contribute to this test suite by adding more test cases or improving the existing ones. Please submit a pull request if you make any enhancements.

## License
This Hangman Game Test Suite is provided under the MIT License.
