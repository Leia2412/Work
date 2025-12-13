import tkinter as tk

def convert_length():
    try:
        inches = float(entry_inch.get())
        centimeters = inches * 2.54
        result_label.config(text=f"{centimeters:.2f} cm")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Create window
window = tk.Tk()
window.title("Length Converter App")
window.geometry("400x400")

# Widgets
title_label = tk.Label(window, text="Inches to Centimeters", font=("Arial", 16))
title_label.pack(pady=20)

entry_inch = tk.Entry(window, font=("Arial", 14))
entry_inch.pack(pady=10)

convert_button = tk.Button(window, text="Convert", font=("Arial", 14), command=convert_length)
convert_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 16))
result_label.pack(pady=20)

# Run window
window.mainloop()
