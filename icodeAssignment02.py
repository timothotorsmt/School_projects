import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

import random
import os

def create_key():
    #this function creates a simple ceasar cipher key for the file. it generates 6 random digits to function as a key, which would aid in the cipher.
    key = random.randint(0,9999999999)
    return str(key)

def encrypt(string, key):
    result = ""
    #depending on the position of the character, the letter will get moved up and down certain amount. 
    for i in range(len(string)):
        char = string[i]
        if char.isupper():
            result += chr((ord(char) + int(key) - 65) % 26 + 65)
        elif char.isalpha():
            result += chr((ord(char) + int(key) - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(string, keys):
    #this function decrypts a given string, given the key. it is basically the reverse of the encrypt function
    return encrypt(string, 26 - int(keys))

def save_dictionary_to_file(dict):
    #this function saves the dictionary to a file 
    #rewrites the entire file
    f = open("dictionary_file.txt", "w")
    f.write(str(dict))
    f.close

def load_dictionary_from_file():
    #this function will load the dictionary from a file
    #if the file does not exist, make the file, if not extract the string and evaluate it
    if os.path.exists("dictionary_file.txt") == False:
        f = open("dictionary_file.txt", "w")
        f.write("{}")
        data = f.read()
        f.close()
        return eval(data)
    else:
        f = open('dictionary_file.txt','rt')
        data = f.read()
        if (data == ""):
            f = open('dictionary_file.txt', 'w')
            f.write("{}")
            f = open('dictionary_file.txt', 'rt')
            data = f.read()
        f.close()
        return eval(data)

def clear():
    #this function helps clear the screen (it doesnt work lol)
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
  
    # for mac and linux(here, os.name is 'posix'
    else:
        _ = os.system('clear')

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    ) #use the askopenfilename dialog from the tkinter.filedialog module to display a file open dialog and store the selected file path to filepath
    if not filepath:
        return #checks to see if the user closes the dialog box or clicks the Cancel button
    txt_edit.delete(1.0, tk.END) #clears the current contents of txt_edit using .delete()
    with open(filepath, "r") as input_file: #used to open the selected file and .read() its contents before storing the text as a string
        text = input_file.read() 
        txt_edit.insert(tk.END, text) #assigns the string text to txt_edit using .insert()
    window.title(f"Simple Text Editor - {filepath}") #sets the title of the window so that it contains the path of the open file

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")], 
    ) #use the asksaveasfilename dialog box to get the desired save location from the user. The selected file path is stored in the filepath variable
    if not filepath:
        return #checks to see if the user closes the dialog box or clicks the Cancel button
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END) #extracts the text from txt_edit with .get() method and assigns it to the variable text
        output_file.write(text) #writes text to the output file
    window.title(f"Simple Text Editor - {filepath}") #updates the title of the window so that the new file path is displayed in the window title

def enter(input):
    userInput = input.get()
    return userInput

def exit(input):
    input.destroy()
    return

def run():
    runWindow = tk.Tk()
    runWindow.title("Run")
    runInstructions = tk.Label(text="File name:")
    runInput = tk.Entry()

    userInput = runInput.get()
    user_input_filename = userInput + ".txt"

    runBtn = tk.Button(
        text = "Run",
        command = createPassword()
        )

    runInstructions.pack()
    runInput.pack()
    runBtn.pack()

    runWindow.mainloop()

def createDecision():
    decisionWindow = tk.Tk()
    decisionInstructions = tk.Label(text = "Make new file?")
    decisionWindow.title("Make new file?")
    yesBtn = tk.Button(
        text = "Yes",
        command = enter("y")
        )
    noBtn = tk.Button(
        text = "No",
        command = enter("n")
        )

    decisionInstructions.pack()
    yesBtn.pack()
    noBtn.pack()

    decisionWindow.mainloop()

def createPassword():
    createPasswordWindow = tk.Tk()
    createPasswordWindow.title("createPassword")
    createPasswordInstructions = tk.Label(text="Create password:")
    createPasswordInput = tk.Entry()

    createPasswordBtn = tk.Button(
        text = "Enter",
        command = enter(createPasswordInput)
        )
    file_password = userInput

    createPasswordInstructions.pack()
    createPasswordInput.pack()
    createPasswordBtn.pack()

    createPasswordWindow.mainloop()

def password():
    passwordWindow = tk.Tk()
    passwordWindow.title("Password")
    passwordInstructions = tk.Label(text="Input password:")
    passwordInput = tk.Entry()

    passwordBtn = tk.Button(
        text = "Enter",
        command = enter(passwordInput)
        )
    user_input_password = userInput

    passwordInstructions.pack()
    passwordInput.pack()
    passwordBtn.pack()

    passwordWindow.mainloop()

def editDecision():
    editWindow = tk.Tk()
    editInstructions = tk.Label(text = "What would you like to do?")
    editWindow.title("Choose")
    writeBtn = tk.Button(
        text = "Write",
        command = enter("w")
        )
    appendBtn = tk.Button(
        text = "Delete",
        command = enter("d")
        )

    user_input = userInput

    editInstructions.pack()
    writeBtn.pack()
    appendBtn.pack()

    editWindow.mainloop()

#main
#password_storage is the main storage dictionary
"""
    password_storage = load_dictionary_from_file()
    fail_state = True
    while (fail_state == True):
        clear()
        run()
        if user_input_filename not in password_storage:
            createDecision()
            if temp_str == "y":
                createPassword()
                file_key = create_key();
                file_dict = {"password" : file_password, "key" : file_key}
                password_storage[user_input_filename] = file_dict
                file = open(user_input_filename, "x")
                save_dictionary_to_file(password_storage)
                print("File successfully created. ")
                continue
            elif temp_str == "n":
                continue
        else:
            password()
            user_wrong_count = 0;
            if password_storage[user_input_filename]["password"] != user_input_password:
                user_wrong_count += 1;
                if user_wrong_count == 3:
                    quit()
            elif password_storage[user_input_filename]["password"] == user_input_password:
                fail_state = False;
                clear()
                f = open(user_input_filename, "rt");
                file_key = password_storage[user_input_filename]["key"]
                if f.read() != '':
                   file_content = f.read()
                   print(decrypt(file_content, file_key))
                   f.close()
                editDecision()
                if (user_input == "w"):
                  f = open(user_input_filename, "a")
                  while (True):
                      value = input()
                      value = encrypt(value, file_key)
                      f.write(value)
                      f.write("\n")
                      if (value == ""):
                          f.close()
                          break;
                      save_dictionary_to_file(password_storage)
                if (user_input == "d"):
                  os.remove(user_input_filename)
                  password_storage.pop(user_input_filename)
                  save_dictionary_to_file(password_storage) 
    document()
"""

def document():
    file = tk.Tk() #window initialise
    file.title(user_input_filename) #window rename
    file.rowconfigure(0, minsize=800, weight=1) #window dimensions
    file.columnconfigure(1, minsize=800, weight=1) #window dimensions

    txt_edit = tk.Text(file) #text box (notepad)
    fr_buttons = tk.Frame(file, relief=tk.RAISED, bd=2) #frame
    btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file) #button initialise

    btn_save.grid(row=0, column=0, sticky="ew", padx=5, pady=5) #setting positions for buttons
    
    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")

    file.mainloop() #so the window doesn't close immediately


#main
#password_storage is the main storage dictionary
password_storage = load_dictionary_from_file()
fail_state = True
while (fail_state == True):
    clear()
    user_input_filename = input("Enter a filename: ")
    user_input_filename = user_input_filename + ".txt"
    if user_input_filename not in password_storage:
        while True:
            temp_str = input("File not found. Make new file? (y/n)")
            if (temp_str == 'y' or temp_str == 'n'):
                break
        temp_str = temp_str.lower()
        if temp_str == "y":
            file_password = input("Enter a user password: ")
            file_key = create_key();
            file_dict = {"password" : file_password, "key" : file_key}
            password_storage[user_input_filename] = file_dict
            file = open(user_input_filename, "x")
            save_dictionary_to_file(password_storage)
            print("File successfully created. ")
            continue
        elif temp_str == "y":
            continue
    else:
        user_input_password = input("Enter a password: ")
        user_wrong_count = 0;
        if password_storage[user_input_filename]["password"] != user_input_password:
            user_wrong_count += 1;
            if user_wrong_count == 3:
                quit()
        elif password_storage[user_input_filename]["password"] == user_input_password:
            fail_state = False;
            clear()
            f = open(user_input_filename, "rt");
            file_key = password_storage[user_input_filename]["key"]
            if f.read() != '':
               file_content = f.read()
               print(decrypt(file_content, file_key))
               f.close()
            user_input = input("\n\nWhat do you want to do today? w/d: ")
            user_input = user_input.upper();
            if (user_input == "W"):
              f = open(user_input_filename, "a")
              while (True):
                  document()
                  value = input()
                  value = encrypt(value, file_key)
                  f.write(value)
                  f.write("\n")
                  if (value == ""):
                      f.close()
                      break;
                  save_dictionary_to_file(password_storage)
            if (user_input == "D"):
              os.remove(user_input_filename)
              password_storage.pop(user_input_filename)
              save_dictionary_to_file(password_storage)
