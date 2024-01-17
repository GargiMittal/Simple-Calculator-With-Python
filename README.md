# Simple-Calculator-With-Python

This is a basic calculator implemented in Python using the Tkinter library.

## How to Use

1. Run the script (`calculator.py`).
2. The calculator window will appear, displaying an entry widget at the top for input and output.
3. Use the numeric buttons (0-9) and arithmetic operators (+, -, *, /) to input your expression.
4. Press the "=" button to calculate the result.
5. Press the "C" button to clear the entry.
6. If there's an error in the input expression, "Error" will be displayed.

## Code Structure

- `on_click(value)`: Appends the clicked button's value to the current input in the entry widget.
- `clear_entry()`: Clears the entry widget.
- `calculate()`: Evaluates the expression in the entry widget and displays the result. Handles errors gracefully.

## Buttons

The calculator has the following buttons:

- Digits: 0-9
- Arithmetic Operators: +, -, *, /
- Other: . (decimal point), = (equals), C (clear)

## Dependencies

- Python 3.x
- Tkinter (included in most Python installations)

## Running the Code

Make sure you have Python installed on your system. Then, run the script using the following command:

```bash
python calculator.py
```
## Notes
- This calculator supports basic arithmetic operations.
- The code uses the eval() function to evaluate expressions, so avoid using it with untrusted input.
- Feel free to modify and enhance the code according to your needs!
