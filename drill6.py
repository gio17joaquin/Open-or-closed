from datetime import *
import os.path
import shutil
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


current = datetime.now()


def moveFiles(file_list):
    for each in file_list:
            mtime = os.path.getmtime(source + '/' + each)
            date = datetime.fromtimestamp(mtime)

            if date > (current-timedelta(1)):
                shutil.copy(source + '/' + each, destination)
                print("\tMoved {}, to {}.\n".format(each, destination))

def load_gui():
    frame = ttk.Frame(root)  
    frame.pack()
    root.wm_title("File Transfer")
    root.minsize(width=600, height=150)


    transButton = ttk.Button(frame,text="Transfer file",command = lambda: moveFiles(files))
    transButton.grid(row=3,column=0,columnspan=2)

    sourceDirButton = ttk.Button(frame,text = "From Folder",
                                command = lambda: fetchDir())
    sourceDirButton.grid(row=1,column=0,padx=10,pady=10)

    destDirButton = ttk.Button(frame,text = "To Folder",
                                 command = lambda:fetchCopyDir())
    destDirButton.grid(row=2,column = 0,padx=10,pady=10)

    global sourceEntry
    sourceEntry = ttk.Entry(frame,width=60)
    sourceEntry.grid(row=1,column=1)
    global destEntry
    destEntry = ttk.Entry(frame,width=60,)
    destEntry.grid(row=2,column=1)

    
def fetchDir():
    direct = filedialog.askdirectory()
    global source
    source = direct
    sourceEntry.insert(0,direct)
    global files
    files = os.listdir(source)

def fetchCopyDir():
    direct = filedialog.askdirectory()
    global destination
    destination = direct
    destEntry.insert(0,direct)


root = Tk()
load_gui()

