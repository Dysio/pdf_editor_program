import tkinter as tk
from tkinter import filedialog, Text
import os
from pypdf2_functions import page_size_dict_func, split_pages

root = tk.Tk()
root.title('PDF size split')
# root.iconbitmap('.icon\\pdf_icon_256x256.ico')

files = []


def addPDF():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("PDF Document", "*.pdf"), ("all files", "*.*")))
    if filename != "":
        files.append(filename)
    # print(filename)
    # print(files)
    for file in files:
        label = tk.Label(frame, text=file, bg="gray")
        label.pack()


def splitPdf():
    for file in files:
        # os.startfile(file)
        split_pages(file, page_size_dict_func(file))

def clear_list():
    files.clear()
    for widget in frame.winfo_children():
        widget.destroy()

def remove_last():
    for widget in frame.winfo_children():
        widget.destroy()

    files.pop(-1)

    for file in files:
        label = tk.Label(frame, text=file, bg="gray")
        label.pack()


canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.05)

openFile = tk.Button(root, text="Open File", padx=10, pady=5,
                     fg="white", bg="#263D42", command=addPDF)
openFile.pack()

splitPdf = tk.Button(root, text="Split PDF's", padx=10, pady=5, fg="white", bg="#263D42", command=splitPdf)
splitPdf.pack()

clearlist = tk.Button(root, text="Clear List", padx=10, pady=10, fg="white", bg="#263D42", command=clear_list)
clearlist.pack()

removelast = tk.Button(root, text="Remove Last", padx=10, pady=10, fg="white", bg="#263D42", command=remove_last)
removelast.pack()

root.mainloop()
