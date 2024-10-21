from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile():
    global fileName
    root.title("Untitled - Notepad")
    fileName=None
    TextArea.delete(1.0, END)

def openFile():
    global fileName
    fileName=askopenfilename(defaultextension="*.txt",filetypes=[("All Files", "*.*"), ("Text Document", "*.txt")])
    if fileName == "":
            fileName = None
            return
    else:
        root.title(os.path.basename(fileName) + " - Notepad")
        TextArea.delete(1.0, END)
        with open(fileName, "r") as f:
            TextArea.insert(1.0, f.read())

def saveFile():
    global fileName
    if fileName == None:
        fileName=asksaveasfilename(initialfile="Untitled.txt", defaultextension="*.txt",filetypes=[("All Files", "*.*"), ("Text Document", "*.txt")])
        # Check if the user canceled the dialog
        if fileName == "":
            fileName = None
            return
        else:
            with open(fileName, "w") as f:
                f.write(TextArea.get(1.0, END))
            root.title(os.path.basename(fileName) + " - Notepad")
    else:
        with open(fileName, "w") as f:
            f.write(TextArea.get(1.0, END))

def cutFile():
    TextArea.event_generate(("<<Cut>>"))

def copyFile():
    TextArea.event_generate(("<<Copy>>"))

def pasteFile():
    TextArea.event_generate(("<<Paste>>"))

def About():
    showinfo("Notepad", "A Simple Notepad")
    
if __name__=="__main__":
    root = Tk()

    root.geometry("900x450")
    root.title("Untitled - Notepad")
    root.minsize(400, 150)
    root.maxsize(1100,800)

    TextArea = Text(root, font="Arial 16")
    fileName = None
    TextArea.pack(expand=True, fill=BOTH)

    MenuBar = Menu(root)

    FileMenu = Menu(MenuBar, tearoff=0)

    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open", command=openFile)
    FileMenu.add_command(label="Save", command=saveFile)

    MenuBar.add_cascade(label="File", menu=FileMenu)

    EditMenu = Menu(MenuBar, tearoff=0)

    EditMenu.add_command(label="Cut", command=cutFile)
    EditMenu.add_command(label="Copy", command=copyFile)
    EditMenu.add_command(label="Paste", command=pasteFile)

    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    Help = Menu(MenuBar, tearoff=0)

    Help.add_command(label="About", command=About)

    MenuBar.add_cascade(label="Help", menu=Help)

    root.config(menu = MenuBar)
    root.mainloop()