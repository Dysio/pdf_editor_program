import tkinter as tk
from tkinter import filedialog, Text
import os
from attributes import page_size_dict_func, split_pages

root = tk.Tk()
root.title('Dysio PDF size split')
root.iconbitmap(r'D:\SONY\Nauka\Python\11.Projekty\01.PDF_Program\pdf_editor_program\pdf_icon_256x256.ico')

files = []

def addPDF():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("PDF Document","*.pdf"), ("all files","*.*")))
    files.append(filename)
    print(filename)
    for file in files:
        if len(file) == 0:
            continue
        label = tk.Label(frame, text=file, bg="gray")
        label.pack()

def runApps():
    for file in files:
        if len(file) == 0:
            continue
        # os.startfile(file)
        split_pages(file, page_size_dict_func(file))

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5,
                     fg="white", bg="#263D42", command=addPDF)
openFile.pack()

runApps = tk.Button(root, text="Split PDF's", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

root.mainloop()