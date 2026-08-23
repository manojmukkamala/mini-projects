# excel_cell_name_finder

Python program to display the Excel cell name when a cell number is
given as input.

Assuming the cell numbers are assigned column-wise, i.e.

```
A1          -      1
B1          -      2
.
.
.
Z1          -     26
.
.
.
XFD1        -   16384
.
.
.
XFD3193     - 52314112
.
.
.
```

If the cell number is given as input, the function returns the cell
name. For example, input `16384` returns `XFD1`.

## How to run

No dependencies (Python 3 standard library only). From this directory:

```bash
python excelcellfinder.py
```

The script runs a few built-in test cases and prints the results.
