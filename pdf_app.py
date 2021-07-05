import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, Text
import os
from pypdf2_functions import page_size_dict_func, split_pages

root = tk.Tk()
root.title('PDF size split')
root.iconbitmap(r'D:\SONY\Nauka\Python\11.Projekty\01.PDF_Program\pdf_editor_program\media\pdf_icon_256x256.ico')
root.geometry("500x700")

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


# canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
# canvas.pack()

# frame = tk.Frame(root, bg="white", width=400, height=400, pady=20)
frame = tk.Canvas(root, bg="white", width=400, height=400)
# frame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.05)
# frame.grid(row=0, column=0, columnspan=3, pady=20, padx=20)
frame.grid(row=0, column=0, columnspan=3, pady=20, padx=20)

# frame_buttons = tk.Frame(root, width=400)
# frame_buttons.place(relwidth=0.8, relheight=0.2, relx=0.1, rely=0.05)

# Create style object
btn_style = ttk.Style()
#Configure a style
btn_style.configure('W.TButton', font=('Arial', 10), foreground='black')

# openFile = tk.Button(root, text="Open File", padx=10, pady=5,fg="white", bg="#263D42", command=addPDF)
openFile = ttk.Button(root, text="Open File", style='W.TButton', command=addPDF)
# openFile.pack()
openFile.grid(row=1,column=0, sticky=(tk.E))

# splitPdf = tk.Button(root, text="Split PDF's", padx=10, pady=5, fg="white", bg="#263D42", command=splitPdf)
split_pdf_btn = ttk.Button(root, text="Split PDF's", style='W.TButton', command=splitPdf)
# split_pdf_btn.pack()
split_pdf_btn.grid(row=2,column=1)

# clearlist = tk.Button(root, text="Clear List", padx=10, pady=10, fg="white", bg="#263D42", command=clear_list)
clearlist = ttk.Button(root, text="Clear List", style='W.TButton', command=clear_list)
# clearlist.pack()
clearlist.grid(row=1, column=1)


# removelast = tk.Button(root, text="Remove Last", padx=10, pady=10, fg="white", bg="#263D42", command=remove_last)
removelast = ttk.Button(root, text="Remove Last", style='W.TButton', command=remove_last)
# removelast.pack()
removelast.grid(row=1, column=2)

root.mainloop()
