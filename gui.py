import os
import os.path
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from main import Main

class MainWindow:
    def __init__(self, root):
        self.root = root
        self._image_url = tk.StringVar()
        self._folder_url = tk.StringVar()
        self.feature = tk.StringVar(value="greyscale")
        self._status = tk.StringVar()
        self._status.set("---")
        
        root.title("Converto")
        root.configure(bg="#eeeeee")

        self.menu_bar = tk.Menu(root, bg="#eeeeee", relief=tk.FLAT)
        self.menu_bar.add_command(label="Help!", command=self.show_help_callback)

        root.configure(menu=self.menu_bar)


        # SELECT AN IMAGE
        self.file_entry_label1 = tk.Label(
            root, text="Enter an Image Path:", bg="#eeeeee", anchor=tk.W
        )
        self.file_entry_label1.grid(
            padx=12,
            pady=(8, 0),
            ipadx=0,
            ipady=1,
            row=0,
            column=0,
            columnspan=4,
            sticky=tk.W + tk.E + tk.N + tk.S,
        )

        self.file_entry1 = tk.Entry(
            root,
            textvariable=self._image_url,
            bg="#fff",
            exportselection=0,
            relief=tk.FLAT,
        )
        self.file_entry1.grid(
            padx=15,
            pady=6,
            ipadx=8,
            ipady=8,
            row=1,
            column=0,
            columnspan=4,
            sticky=tk.W + tk.E + tk.N + tk.S,
        )

        self.select_btn1 = tk.Button(
            root,
            text="SELECT AN IMAGE",
            command=self.selectfolder1_callback,
            width=42,
            bg="#3498db",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT,
        )
        self.select_btn1.grid(
            padx=15,
            pady=8,
            ipadx=24,
            ipady=6,
            row=2,
            column=0,
            columnspan=4,
            sticky=tk.W + tk.E + tk.N + tk.S,
        )

        # SELECT DESTINATION FOLDER
        self.file_entry_label2 = tk.Label(
            root, text="Enter Output Folder Path:", bg="#eeeeee", anchor=tk.W
        )
        self.file_entry_label2.grid(
            padx=12,
            pady=(8, 0),
            ipadx=0,
            ipady=1,
            row=3,
            column=0,
            columnspan=4,
            sticky=tk.W + tk.E + tk.N + tk.S,
        )

        self.file_entry2 = tk.Entry(
            root,
            textvariable=self._folder_url,
            bg="#fff",
            exportselection=0,
            relief=tk.FLAT,
        )
        self.file_entry2.grid(
            padx=15,
            pady=6,
            ipadx=8,
            ipady=8,
            row=4,
            column=0,
            columnspan=4,
            sticky=tk.W + tk.E + tk.N + tk.S,
        )
        
        self.select_btn2 = tk.Button(
            root,
            text="SELECT OUTPUT FOLDER",
            command=self.selectfolder2_callback,
            width=42,
            bg="#3498db",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT,
        )
        self.select_btn2.grid(
            padx=15,
            pady=8,
            ipadx=24,
            ipady=6,
            row=5,
            column=0,
            columnspan=4,
            sticky=tk.W + tk.E + tk.N + tk.S,
        )

        # RADIO BUTTON
        self.select_feature_greyscale = tk.Radiobutton(
            root, 
            text="Greyscale", 
            variable=self.feature, 
            value="greyscale"
        )

        self.select_feature_greyscale.grid(
            padx=10,
            pady=8,
            ipadx=24,
            ipady=6,
            row=8,
            column=0,
            columnspan=1,
            sticky=tk.W + tk.E + tk.N + tk.S,
        )

        self.select_feature_smoothing = tk.Radiobutton(
            root, 
            text="Smoothing", 
            variable=self.feature, 
            value="smoothing"
        )
        
        self.select_feature_smoothing.grid(
            row=8,
            column=2,
            columnspan=1,
            sticky=tk.W + tk.E + tk.N + tk.S,
        )

        self.select_feature_compress = tk.Radiobutton(
            root, 
            text="Compress", 
            variable=self.feature, 
            value="compress"
        )
        
        self.select_feature_compress.grid(
            row=8,
            column=1,
            columnspan=1,
            sticky=tk.W + tk.E + tk.N + tk.S,
        )

        

        # START AND RESET BUTTON
        self.convert_btn = tk.Button(
            root,
            text="START",
            command=self.execute,
            bg="#27ae60",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT,
        )

        self.convert_btn.grid(
            padx=15,
            pady=8,
            ipadx=24,
            ipady=6,
            row=12,
            column=0,
            columnspan=2,
            sticky=tk.W + tk.E + tk.N + tk.S,
        )

        self.reset_btn = tk.Button(
            root,
            text="CLEAR STATUS",
            command=self.reset_callback,
            bg="#717d7e",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT,
        )
        self.reset_btn.grid(
            padx=15,
            pady=8,
            ipadx=24,
            ipady=6,
            row=12,
            column=2,
            columnspan=2,
            sticky=tk.W + tk.E + tk.N + tk.S,
        )

        # STATUS LABEL
        self.status_label = tk.Label(
            root,
            textvariable=self._status,
            bg="#eeeeee",
            anchor=tk.W,
            justify=tk.LEFT,
            relief=tk.FLAT,
            wraplength=350,
        )
        self.status_label.grid(
            padx=12,
            pady=(0, 12),
            ipadx=0,
            ipady=1,
            row=14,
            column=0,
            columnspan=4,
            sticky=tk.W + tk.E + tk.N + tk.S,
        )

    #FUNCTION GUI

    def selectfolder1_callback(self):
        try:
            name = filedialog.askopenfilename()
            self._image_url.set(name)
        except Exception as e:
            self._status.set(e)
            self.status_label.update()

    def selectfolder2_callback(self):
        try:
            name = filedialog.askdirectory()
            self._folder_url.set(name)
        except Exception as e:
            self._status.set(e)
            self.status_label.update()

    def show_help_callback(self):
        messagebox.showinfo(
            "Help!",
            """1. CHOOSE AN IMAGE FROM YOUR COMPUTER
2. CHOOSE OUTPUT DESTINATION DIRECTORY
3. SELECT FEATURE YOU WANT
4. PRESS CONVERT BUTTON
5. THE CONVERTED IMAGE ALREADY IN YOUR DESTINATION DIR
            """,
        )

    def execute(self):
        feature = self.feature.get()
        image_url = self._image_url.get()
        folder_url = self._folder_url.get()
    
        try:
            Main.execute(feature, image_url, folder_url)
            msg = "IMAGE is saved at " + folder_url
            self._status.set(msg)
            messagebox.showinfo(
            "INFO", msg
            )
        except:
            self._status.set("found error")
            messagebox.showerror(
            "ERROR", "found error"
            )
        
    def reset_callback(self):
        self._image_url.set("")
        self._folder_url.set("")
        self._status.set("---")

ROOT = tk.Tk()
ROOT.resizable(height=False, width=False)
folder_path_1 = StringVar()
folder_path_2 = StringVar()
MAIN_WINDOW = MainWindow(ROOT)
ROOT.mainloop()
        
