import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.messagebox
import time

import random
import os

def create_key():
    #this function creates a simple ceasar cipher key for the file. it generates 6 random digits to function as a key, which would aid in the cipher.
    key = 26
    while ((int(key) % 26 == 0)):
        key = random.randint(1000000000,9999999999)
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
    f.write(encrypt(str(dict), 111))
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
        data = decrypt(f.read(), 111)
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

#main
#password_storage is the main storage dictionary

def document():
    def save_file():
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")], 
        ) #use the asksaveasfilename dialog box to get the desired save location from the user. The selected file path is stored in the filepath variable
        if not filepath:
            return #checks to see if the user closes the dialog box or clicks the Cancel button
        with open(filepath, "w") as output_file:
            text = encrypt(txt_edit.get(1.0, tk.END), file_key) #extracts the text from txt_edit with .get() method and assigns it to the variable text
            output_file.write(text) #writes text to the output file

    fileWindow = tk.Tk() #window initialise
    fileWindow.title(user_input_filename) #window rename
    fileWindow.rowconfigure(0, minsize=800, weight=1) #window dimensions
    fileWindow.columnconfigure(1, minsize=800, weight=1) #window dimensions

    txt_edit = tk.Text(fileWindow) #text box (notepad)
    fr_buttons = tk.Frame(fileWindow, relief=tk.RAISED, bd=2) #frame
    btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file) #button initialise
    btn_delete = tk.Button(fr_buttons, text="Delete file", command = delete)

    btn_save.grid(row=0, column=0, sticky="ew", padx=5, pady=5) #setting positions for buttons
    btn_delete.grid(row=1, column=0, sticky="ew", padx=5)
    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")

    txt_edit.insert('1.0', (decrypt(file_content, file_key))) #read the existing text

    fileWindow.mainloop() #so the window doesn't close immediately

def delete():
    #if the file is in the file directory, delete the file
    if user_input_filename in os.listdir(): 
        os.remove(user_input_filename)
        password_storage.pop(user_input_filename)
        save_dictionary_to_file(password_storage) 
        tkinter.messagebox.showinfo('Removed!', 'Successfully Removed!')
        quit()
    else:
        tkinter.messagebox.showerror('Error!', 'File not found!')

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
            temp_str = input("File not found. Make new file? (y/n): ")
            temp_str = temp_str.lower()
            if (temp_str == 'y' or temp_str == 'n'):
                break
        if temp_str == "y":
            file_password = input("Enter a user password: ")
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
        user_input_password = input("Enter a password: ")
        while password_storage[user_input_filename]["password"] != user_input_password:
            user_input_password = input("Wrong password. Please try again.\nEnter a password: ")
            user_wrong_count += 1;
            if user_wrong_count == 3:
                quit()
        user_wrong_count = 0;
        fail_state = False;
        file_key = password_storage[user_input_filename]["key"]
        file_content = open(user_input_filename).read()
        document()
        save_dictionary_to_file(password_storage)
