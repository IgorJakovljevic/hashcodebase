# hashcodebase
Base Code for the Google Hash Code Project

# How To Use?

## Datastrem

### Class for data handling

<ul>
    <li>Has a "open" function used for reading the problem file and returning a data structure</li>
    <li>Has a "write" function used for writing a result data structure the solution file</li>
</ul>

## Solver

### Class for algorithm implementation

<ul>
<li>"solve" implements the algorithm where the input data comes from the datastrem </li>
<li>"score" implement this to calculate the score of the solver</li>
<li>"error" implement this to calculate the error of the solver</li>
</ul>

## Setup and Run the solver project
```bash
pip install requirements.txt
python run.py
```

## How to execute the "2019 Implementation"
```bash
python run_2019.py
```
