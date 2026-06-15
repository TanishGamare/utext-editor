from tkinter import * 
import tkinter.filedialog as fd 
import tkinter.messagebox as mb 

from PIL import Image, ImageTk
import os 


#Initializing the window to create python text editor 
root = Tk()
root.title("NotePad")
root.geometry("800x500")
root.resizable(0, 0)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

icon = ImageTk.PhotoImage(Image.open('Notepad.png'))
root.iconphoto(False, icon)


#Finalizing the window
root.update
root.mainloop()


#Initializing all of the functions needed
def openfile():
    file = fd.askopenfilename(defaultextension='.txt', filetypes=[('All Files', '*.*'), ("Text File", "*.txt*")])

    if file != '':
        root.title(f"{os.path.basename(file)}")
        text_area.delete(1.0, END)
        with open(file, "r") as file_:
            text_area.insert(1.0, file_.read())
            file.close()
    else:
        file = None 

def open_new_file():
    root.title("Untitled - Notepad")
    text_area.delete(1.0, END)

def save_file(): 
    global text_area 
    file = text_area.get(1.0, END)
    if file == '':
        file = None 
    else: 
        file = open(file, "w")
        file.write(text_area.get(1.0, END))
        file.close 

    if file is None: 
        file = fd.asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt')
filetypes=[("Text file", "*.txt"), ("Word Document", '*,docx*'), ("PDF", "*.pdf*")]) 


