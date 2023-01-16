# Simple and Secure Password Generator by Alper Celik
# Due to security issues, random() method is not used.

import secrets
import string as s
import tkinter as tk
import clipboard as cb

def passwordGenerator(symbol: bool, uppercs: bool, length: int):

    combin = s.digits + s.ascii_lowercase

    #for security issues, choose it as True -use uppercase-
    if uppercs:
        combin += s.ascii_uppercase
    #also for increasing security, symbols are essential
    if symbol:
        combin += s.punctuation

    combinLength = len(combin)

    newPassword = ""
    for _ in range(length):
        newPassword += combin[secrets.randbelow(combinLength)]

    return newPassword


def main():

    yourPassword = passwordGenerator(symbol=True, uppercs=True, length=12) # symbols added, uppercases added, 12-length secure password
    print("Here is the secure password: ", yourPassword) #to control on terminal

    # GUI Side, tkinter
    root = tk.Tk();

    root.geometry("500x300")
    root.title("Simple & Secure Password Generator")

    label1 = tk.Label(root, text="\n\nHere is your 12-character secure password\n", font=('Arial', 18))
    passLabel = tk.Label(root, text=yourPassword, font=('New Roman', 24))
    label1.pack()
    passLabel.pack(padx=30, pady=40)

    #copy button of the created password
    copyBtn = tk.Button(root, text="Copy Your New Password")
    copyBtn.pack()

    def copyToClipboard(stringToCopy: str):
        cb.copy(stringToCopy)
        label3 = tk.Label(root, text="Copied!", font=('Arial', 14))
        label3.pack(padx=30, pady=20)

    copyBtn.bind("<Button-1>", lambda e: copyToClipboard(yourPassword))


    root.mainloop()


if __name__ == "__main__":
    main()