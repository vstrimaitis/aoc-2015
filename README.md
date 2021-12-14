# Advent of Code 2015 Solutions

This repository contains the solutions for the Advent of Code 2015 puzzles.

I only got around to actually solving the problems at the end of 2021, so this is long overdue :sweat_smile:

## Running the solutions

To run the solution for any given day, run the corresponding Python script:

```bash
python day_XY.py
```

The repository also comes with a suite of unit tests. To run them all, use this command:

```bash
python -m unittest discover .
```

Since some tests take quite some time to run, it might be useful to run the tests for a single day.
This can be achieved by using the following command (`XY` here is the two digit day number):

```bash
python -m unittest discover -p "*XY*" .
```
