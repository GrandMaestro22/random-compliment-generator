# Random Compliment Generator

A simple Python command-line program that asks for your name, gives you a random compliment, and lets you choose whether to get another one.

## What The Program Does

- Stores a list of compliments in Python.
- Uses `random.choice()` to pick one compliment each round.
- Asks the user for their name using `input()`.
- Validates input so blank names are not accepted.
- Repeats in a loop until the user answers `n` (or anything other than `y/yes`) when asked to continue.

## Skills I Used

- Python lists to store text data.
- Importing and using the `random` module.
- `while True` loops for repeated interaction.
- `if` conditions for input validation and flow control.
- String methods like `.strip()` and `.lower()` for cleaner user input handling.
- Formatted string literals (f-strings) for readable output.

## What I Learned

- How to build an interactive command-line app that responds to user input.
- How loop control with `break` can stop a program cleanly.
- Why input validation improves user experience.
- How normalizing user input (for example with `.lower()`) makes logic more reliable.
- How small programs can still demonstrate strong programming fundamentals.

## How To Run

1. Make sure Python is installed.
2. In this project folder, run:

```bash
python random-compliment.py
```

## Example

```text
What is your name? Alex
Alex, You bring good energy wherever you go.
Would you like another compliment? (y/n): y
What is your name? Alex
Alex, Your creativity has no off switch.
Would you like another compliment? (y/n): n
Thanks for using the compliment generator. Have a great day!
```