#!/usr/bin/python3
# YoutubeMedia
# version 1.0
# https://github.com/ruslansco/YoutubeMedia
# Start Date: 12/10/2021
# Rev Date: -

import tkinter as tk
import tkinter.scrolledtext as tkst
from datetime import datetime
import sys,time,random

class Console:
    """================= Class creates a text field for reciveing and displaying text. ================="""
    def __init__(self, root):
        self.console = tkst.Text(root, height=15, width=55, fg="#fff", bg="#2e465e", font=("Calibri", 11),
                            borderwidth=1, relief="solid")
        self.create_console()
        self.greetings()

    def create_console(self):
        # Placing cursor in the text area
        self.console.focus()
        self.console.bind("<1>", lambda e: 'break')
        self.console.place(x=6, y=220)

    def slow_type(text):
        typing_speed = 300  # wpm
        for l in text:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(random.random() * 10.0 / typing_speed)
        print('')

    def greetings(self):
        return self.console.insert(tk.END, ("Welcome to YoutubeMedia Pro. " \
               "\n\n1) Paste a youtube URL you'd like to download from above." \
               "\n2) Select a video resolution." \
               "\n3) Click on the download button below.\n\n\n"))

    def print_text(self, text):
        #Pushes the scrollbar and focus of text to the end of the text input.
        self.console.yview(tk.END)
        return self.console.insert(tk.END, (datetime.now().strftime(
                '[%H:%M:%S]') + str(text)))

    def lock_console(self):
        return self.console.configure(state='disabled')

    def clean_console(self):
        return self.console.delete(1.0, tk.END)