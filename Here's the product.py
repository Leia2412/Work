import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_box.delete("1.0", tk.END)  # clear previous result
        result_box.insert(tk.END, f"Product: {product}")
    except ValueError:
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.geometry("400x300")
root.title("Getting Started with Widgets")

# Description label
desc_label = tk.Label(root, text="This app multiplies two numbers.")
desc_label.pack(pady=10)

# Input labels and entries
label1 = tk.Label(root, text="Enter first number:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter second number:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Button
calc_button = tk.Button(root, text="Calculate Product", command=calculate_product)
calc_button.pack(pady=10)

# Result text box
result_box = tk.Text(root, height=3, width=30)
result_box.pack()

root.mainloop()
