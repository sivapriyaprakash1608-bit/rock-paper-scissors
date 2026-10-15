# Rock-Paper-Scissors

A command-line Rock-Paper-Scissors game written in Python. The player plays 5 rounds against the computer, and the final result is decided by comparing both scores.

## Rules

- Rock breaks Scissors
- Scissors cut Paper
- Paper covers Rock
- Same choice by both is a tie

## Features

- Computer chooses randomly each round
- Score kept for both the player and the computer
- Input is not case-sensitive (`Rock`, `ROCK` and `rock` all work)
- Invalid input is rejected without using up a round
- Final result: win, loss or draw, with both scores shown

## Concepts Used

- `random.choice()` with a list
- `while` loop with `continue`
- `if / elif / else` with `and` conditions
- String method `.lower()`
- Membership check with `not in`
- Counters and score tracking

## How to Run

1. Install [Python 3](https://www.python.org/downloads/)
2. Download `rock_paper_scissors.py`
3. Open a terminal in the file's folder and run:

```
python rock_paper_scissors.py
```

## Sample Output

```
Choose any one of the options: rock/paper/scissors: rock
Paper covers rock...computer wins!!!
Choose any one of the options: abc
Invalid choice, try again
Choose any one of the options: scissors
Scissors cuts the paper...player wins!!!
...
You won
Player: 3 Computer: 2
```

## Possible Improvements

- Show the number of ties at the end
- Show what the computer chose each round
- Ask "Play again?" after the game ends
- Let the player choose the number of rounds

## Author

Sivapriya M S
