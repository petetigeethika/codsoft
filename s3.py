import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation
def perform_calculation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError as e:
        messagebox.showerror("Math Error", str(e))

# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place labels, entries, and buttons
tk.Label(root, text="Enter the first number:").grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter the second number:").grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Choose an operation:").grid(row=2, column=0, padx=10, pady=5)

operation_var = tk.StringVar()
operation_var.set("+")

operations_frame = tk.Frame(root)
operations_frame.grid(row=2, column=1, padx=10, pady=5)

tk.Radiobutton(operations_frame, text="+", variable=operation_var, value="+").pack(side="left")
tk.Radiobutton(operations_frame, text="-", variable=operation_var, value="-").pack(side="left")
tk.Radiobutton(operations_frame, text="*", variable=operation_var, value="*").pack(side="left")
tk.Radiobutton(operations_frame, text="/", variable=operation_var, value="/").pack(side="left")

calculate_button = tk.Button(root, text="Calculate", command=perform_calculation)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
