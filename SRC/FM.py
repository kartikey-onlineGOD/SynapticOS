#File Manager

from tkinter import *
import shutil         
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb
import tkinter.font as font

def open_window():
    read=easygui.fileopenbox()
    return read

# open file function
def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmation', "File not found!")

# copy file function
def copy_file():
    source1 = open_window()
    destination1=filedialog.askdirectory()
    shutil.copy(source1,destination1)
    mb.showinfo('confirmation', "File Copied !")

# delete file function
def delete_file():
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)             
    else:
        mb.showinfo('confirmation', "File not found !")

# rename file function
def rename_file():
    chosenFile = open_window()
    path1 = os.path.dirname(chosenFile)
    extension=os.path.splitext(chosenFile)[1]
    print("Enter new name for the chosen file")
    newName=input()
    path = os.path.join(path1, newName+extension)
    print(path)
    os.rename(chosenFile,path) 
    mb.showinfo('confirmation', "File Renamed !")

# move file function
def move_file():
    source = open_window()
    destination =filedialog.askdirectory()
    if(source==destination):
        mb.showinfo('confirmation', "Source and destination are same")
    else:
        shutil.move(source, destination)  
        mb.showinfo('confirmation', "File Moved !")

# function to make a new folder
def make_folder():
    newFolderPath = filedialog.askdirectory()
    print("Enter name of new folder")
    newFolder=input()
    path = os.path.join(newFolderPath, newFolder)  
    os.mkdir(path)
    mb.showinfo('confirmation', "Folder created !")

# function to remove a folder
def remove_folder():
    delFolder = filedialog.askdirectory()
    os.rmdir(delFolder)
    mb.showinfo('confirmation', "Folder Deleted !")

def main():
    
    root = Tk()

    Label(root, text="              File Manager                  ", font=("Jokerman", 16), fg = "Orange").grid(row = 5, column = 2)
    Button(root, text = "    Open a File    ", command = open_file, background= "Grey", fg = "Orange", font=("Jokerman", 16)).grid(row=15, column =2)
    Button(root, text = "    Copy a File    ", command = copy_file, background= "grey", fg = "Orange", font=("Jokerman", 16)).grid(row = 30, column = 2)
    Button(root, text = "   Delete a File   ", command = delete_file, background= "grey", fg = "Orange", font=("Jokerman", 16)).grid(row = 45, column = 2)
    Button(root, text = " Rename a File  ", command = rename_file, background= "grey", fg = "Orange", font=("Jokerman", 16)).grid(row = 60, column = 2)
    Button(root, text = "    Move a File    ", command = move_file, background= "grey", fg = "Orange", font=("Jokerman", 16)).grid(row = 75, column =2)
    Button(root, text = "Remove a Folder", command = remove_folder, background= "grey", fg = "Orange", font=("Jokerman", 16)).grid(row = 90, column =2)
    root.mainloop()
