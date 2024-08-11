import tkinter as tk
from tkinter import messagebox

# Function for Caesar Cipher
def caesar_cipher(message, shift, mode='encrypt'):
    result = ""

    # Adjusting the shift value for decryption.
    # For encryption it will be same, but for decryption in will be opposite in sign.
    if mode == 'decrypt':
        shift = -shift

    # Traverse through each character in the message.
    for char in message:
        # To Encrypt & Decrypt only characters.
        if char.isalpha():
            # Preserve case by using the appropriate offset.
            offset = 65 if char.isupper() else 97
            # Shift character and wrap around the alphabet using modulo.
            # Module with total no.of alphabets will make sure that shifted character stays within the range.
            shifted_char = chr((ord(char) - offset + shift) % 26 + offset)
            result += shifted_char
        else:
            # Special Characters or Numbers will be unchanged.
            result += char

    return result

# Function to handle encryption or decryption based on user choice
def process_cipher():
    message = text_message.get("1.0", tk.END).strip()  # Get text from Text widget and strip newline characters.
    shift = entry_shift.get()

    # Checking if the message or shift value is not filled.
    if not message or not shift.isdigit():
        messagebox.showerror("Input Error", "Please enter a valid message and numeric shift value.")
        return

    # Taking inputs (shift value, mode).
    shift = int(shift)
    mode = var_mode.get()

    if mode == 1:
        result = caesar_cipher(message, shift, mode='encrypt')
    elif mode == 2:
        result = caesar_cipher(message, shift, mode='decrypt')

    text_result.delete("1.0", tk.END)  # Clear the result Text widget before inserting new result.
    text_result.insert("1.0", result)  # Display the result in the result Text widget.

# Setting up the main application window or main frame.
root = tk.Tk()
root.title("Caesar Cipher")

# Message label and message text field.
label_message = tk.Label(root, text="Enter the message:")
label_message.pack(pady=5)
text_message = tk.Text(root, height=5, width=50)
text_message.pack(pady=5)

# Frame for shift value and radio buttons (to display them in same the line).
frame_controls = tk.Frame(root)
frame_controls.pack(pady=5)

# Shift label and entry field.
label_shift = tk.Label(frame_controls, text="Shift value:")
label_shift.pack(side=tk.LEFT, padx=10)
entry_shift = tk.Entry(frame_controls, width=5)
entry_shift.pack(side=tk.LEFT, padx=10)

# Radio buttons for mode selection (Encrypt/Decrypt) inside the same frame.
var_mode = tk.IntVar(value=1)  # By default to Encrypt
radio_encrypt = tk.Radiobutton(frame_controls, text="Encrypt", variable=var_mode, value=1)
radio_encrypt.pack(side=tk.LEFT, padx=10)
radio_decrypt = tk.Radiobutton(frame_controls, text="Decrypt", variable=var_mode, value=2)
radio_decrypt.pack(side=tk.LEFT, padx=10)

# Button to execute the cipher process
button_process = tk.Button(root, text="Process", command=process_cipher)
button_process.pack(pady=10)

# Result label and result text field
label_result = tk.Label(root, text="Result:")
label_result.pack(pady=5)
text_result = tk.Text(root, height=5, width=50)
text_result.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
