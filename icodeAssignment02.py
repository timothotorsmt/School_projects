import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def document():
    file = tk.Tk() #window initialise
    file.title("file name") #window rename
    file.rowconfigure(0, minsize=800, weight=1)
    file.columnconfigure(1, minsize=800, weight=1)

    txt_edit = tk.Text(file)
    fr_buttons = tk.Frame(file, relief=tk.RAISED, bd=2)
    btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
    btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)
    
    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")

    file.mainloop()

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

def enter(input):
    userInput = input.get()
    return userInput

def run():
    runStatus = True
    runWindow = tk.Tk()
    runWindow.title("Run")
    runInstructions = tk.Label(text="File name:")
    runInput = tk.Entry()

    runBtn = tk.Button(
        text = "Run",
        command = enter(runInput)
        )

    runInstructions.pack()
    runInput.pack()
    runBtn.pack()

    runWindow.mainloop()

def password():
    passwordWindow = tk.Tk()
    passwordWindow.title("Password")
    passwordInstructions = tk.Label(text="Input password:")
    passwordInput = tk.Entry()

    passwordBtn = tk.Button(
        text = "Enter",
        command = enter(passwordInput)
        )

    passwordInstructions.pack()
    passwordInput.pack()
    passwordBtn.pack()

    passwordWindow.mainloop()

def decision():
    decisionWindow = tk.Tk()
    decisionInstructions = tk.Label(text = "Make new file?")
    decisionWindow.title("Make new file?")
    yesBtn = tk.Button(
        text = "Yes"
        )
    noBtn = tk.Button(
        text = "No"
        )

    decisionInstructions.pack()
    yesBtn.pack()
    noBtn.pack()

    decisionWindow.mainloop()

def create():
    createWindow = tk.Tk()
    createWindow.title("Create new file")
    createInstructions = tk.Label(text="Create new file:")
    createInput = tk.Entry()

    createBtn = tk.Button(
        text = "Enter",
        command = enter(createInput)
        )

    createInstructions.pack()
    createInput.pack()
    createBtn.pack()

    createWindow.mainloop()

def createPassword():
    createPasswordWindow = tk.Tk()
    createPasswordWindow.title("createPassword")
    createPasswordInstructions = tk.Label(text="Create password:")
    createPasswordInput = tk.Entry()

    createPasswordBtn = tk.Button(
        text = "Enter",
        command = enter(createPasswordInput)
        )

    createPasswordInstructions.pack()
    createPasswordInput.pack()
    createPasswordBtn.pack()

    createPasswordWindow.mainloop()
 

run()
password()
decision()
create()
createPassword()
document()