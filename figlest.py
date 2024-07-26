import tkinter as tk
from tkinter import messagebox
import pyfiglet
import pyperclip

def generate_figlet():
    input_text = text_input.get()
    if input_text:
        figlet_text = pyfiglet.figlet_format(input_text)
        text_output.delete('1.0', tk.END)
        text_output.insert(tk.END, figlet_text)
    else:
        messagebox.showwarning("Input Error", "Please enter some text.")

def copy_to_clipboard():
    figlet_text = text_output.get('1.0', tk.END)
    if figlet_text.strip():
        pyperclip.copy(figlet_text)
        messagebox.showinfo("Copied", "Figlet text copied to clipboard.")
    else:
        messagebox.showwarning("Output Error", "There is no Figlet text to copy.")

root = tk.Tk()
root.title("Figlet Text Generator")
root.resizable(False, False)
# Create input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Input label and entry
input_label = tk.Label(input_frame, text="Enter Text:")
input_label.pack(side=tk.LEFT, padx=5)
text_input = tk.Entry(input_frame, width=40)
text_input.pack(side=tk.LEFT, padx=5)

# Generate button
generate_button = tk.Button(input_frame, text="Generate", command=generate_figlet)
generate_button.pack(side=tk.LEFT, padx=5)

# Create output frame
output_frame = tk.Frame(root)
output_frame.pack(pady=10)

# Output text box
text_output = tk.Text(output_frame, width=80, height=20)
text_output.pack()

# Copy button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Run the application
root.mainloop()

print("copyright Yasin Horani (～￣▽￣)～  -.-- .- ... .. -. / .... --- .-. .- -. ..")







