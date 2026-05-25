from tkinter import *
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result_label.config(text="Cannot divide by zero")
                return
            result = num1 / num2
        else:
            result_label.config(text="Select operation")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Enter valid numbers")
root = Tk()
root.title("Simple Calculator")
root.geometry("350x300")
root.config(bg="lightblue")

heading = Label(root, text="Simple Calculator", font=("Arial", 18, "bold"), bg="lightblue")
heading.pack(pady=10)

Label(root, text="Enter First Number:", bg="lightblue", font=("Arial", 12)).pack()
entry1 = Entry(root, font=("Arial", 12))
entry1.pack(pady=5)

Label(root, text="Enter Second Number:", bg="lightblue", font=("Arial", 12)).pack()
entry2 = Entry(root, font=("Arial", 12))
entry2.pack(pady=5)

Label(root, text="Select Operation:", bg="lightblue", font=("Arial", 12)).pack()

operation_var = StringVar()
operation_var.set("+")  # default value

operations = OptionMenu(root, operation_var, "+", "-", "*", "/")
operations.pack(pady=5)

calc_button = Button(root, text="Calculate", font=("Arial", 12, "bold"),
                     bg="green", fg="white", command=calculate)
calc_button.pack(pady=15)

result_label = Label(root, text="Result: ", font=("Arial", 14, "bold"), bg="lightblue")
result_label.pack(pady=10)
root.mainloop()