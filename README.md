# Unit Converter

A simple command-line unit converter in Python.

- **Length:** mm, cm, m, km, in, ft, yd, mi
- **Weight:** g, kg, oz, lb
- **Temperature:** c, f, k

## Run

Command-line version:

```
python converter.py
```

GUI version (window with dropdowns and a Convert button, uses built-in `tkinter`):

```
python gui.py
```

## Example

```
Category (length, weight, temperature): length
Value: 5
From (mm, cm, m, km, in, ft, yd, mi): km
To (mm, cm, m, km, in, ft, yd, mi): mi
5 km = 3.107 mi
Convert another? (y/n): n
```

## Test

```
python -m unittest
```

## How it works

- One one-line function per category (`convert_length`, `convert_weight`, `convert_temperature`).
- Length and weight use dictionaries of factors to a base unit (meters, kilograms), so adding a unit is one line.
- Temperature converts to Celsius first, then to the target unit, using two small lookup tables.
- `ask()` validates input in a loop so bad entries don't crash the program.
