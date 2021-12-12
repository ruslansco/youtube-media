#!/usr/bin/python3
# YoutubeMedia
# version 1.0
# https://github.com/ruslansco/YoutubeMedia
# Start Date: 12/10/2021
# Rev Date: -

import tkinter as tk
import terminal
from pathlib import Path, PureWindowsPath
import os
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk
import api
import webbrowser
import time
import time
from threading import *

class Root(tk.Frame):
    """================= Class creates the primary interface. ================="""

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.create_root()
        self.create_navbar()
        self.create_footer()
        self.create_entry()
        self.create_check_buttons()
        self.create_clear_button()
        self.create_start_button()
        self.run = terminal.Console(root)

    def create_root(self):
        panel = tk.Label(root, bg="#15202b", borderwidth=1, relief="solid")
        panel.pack(side="bottom", fill="both", expand=1)
        root.title("YoutubeMedia Pro")  # Title
        root.geometry("400x670+0+0")  # Size
        # Gets requested values of height and width.
        width = root.winfo_reqwidth()
        height = root.winfo_reqheight()
        # Gets both screen width/height and window width/height
        position_right = int(root.winfo_screenwidth() / 3 - width/ 3)
        position_down = int(root.winfo_screenheight() / 3 - height / 3)
        # Positions main window frame in the center of screen.
        root.geometry("+{}+{}".format(position_right,position_down))
        # Window Opacity 0.0-1.0
        root.wm_attributes("-alpha", "0.99")

        def savelastclick_position(event):
            global lastclick_x, lastclick_y
            lastclick_x = event.x
            lastclick_y = event.y
        def dragging(event):
            x, y = event.x - lastclick_x + root.winfo_x(), event.y - lastclick_y + root.winfo_y()
            root.geometry("+%s+%s" % (x, y))

        root.overrideredirect(True)
        # Always keep window on top of others
        root.attributes('-topmost', True)
        root.bind('<Button-1>', savelastclick_position)
        root.bind('<B1-Motion>', dragging)
        # Fixed size
        root.resizable(width=False, height=False)

    def create_navbar(self):
        """================= Creates logo in the root window ================="""
        # Header Title
        header_title = tk.Label(root, font=("Comic Sans MS", 21, "bold"), text="YoutubeMedia Pro", fg="#fff", bg="#000",
                             borderwidth=1, relief="solid")
        header_title.pack(side=tk.TOP,fill=tk.BOTH)
        
        # Youtube Icon
        youtube_icon = ImageTk.PhotoImage(file='icons/youtube.png')
        youtube_icon_label = Label(header_title, image=youtube_icon, borderwidth=1, relief="solid")
        youtube_icon_label.image = youtube_icon
        youtube_icon_label.place(x=0, y=-4)
        # Quit Button
        quit_icon = ImageTk.PhotoImage(file='icons/quit.jpg')
        quit_icon_button = Button(header_title, image=quit_icon, bg="#000", borderwidth=1, relief="solid",
                                  command=lambda: self.close_program())
        quit_icon_button.image = quit_icon
        quit_icon_button.place(x=345, y=-1)

    def create_footer(self):
        """================= ================= """
        # Footer Text
        footer_text = tk.Label(root, font=("Calibri", 13, "bold"), text="https://github.com/ruslansco/youtube-media" , fg="#fff", bg="#15202b", cursor="hand2")
        footer_text.place(x=35, y=645)
        footer_text.bind("<Button-1>", lambda e: self.click_url(self, "https://github.com/ruslansco"))
        
        # Github Button
        github_icon = ImageTk.PhotoImage(file='icons/github.png')
        github_icon_label = Label(root, image=github_icon, bg="#15202b", cursor="hand2")
        github_icon_label.image = github_icon
        github_icon_label.place(x=2, y=640)
        github_icon_label.bind("<Button-1>", lambda e: self.click_url(self, "https://github.com/ruslansco"))

    def create_entry(self):  
        """================= Creates fields in the root window ================="""
        global acc_input

        # Title 
        acc_title = tk.Label(root, text="Paste YouTube URL", font=("Comic Sans MS", 15, "bold"), fg="#fff",
                          bg="#15202B")
        acc_title.place(x=80, y=60)

        acc_input = tk.Entry(root, bd=1, fg="#fff", bg="#2e465e", font=("Arial", 12),
                                 borderwidth=1, relief="solid", validate="key")
        #acc_input['validatecommand'] = (acc_input.register(validate_input),'%S', '%d')
        acc_input.place(x=80, y=100)
        acc_input.focus_set()  # Set cursor focus to the entry.

    def create_check_buttons(self):
        """================= Creates 3 check-buttons in root window for downloading media: Pictures, Videos, Stories. ================="""

        choice_pictures = tk.IntVar()
        choice_videos = tk.IntVar()

        # Title - "Video Resolution"
        media_title = tk.Label(root, text="Video Resolution", font=("Comic Sans MS", 13, 'bold'),
                               fg="#fff", bg="#15202B")
        media_title.place(x=100, y=135)

        # Checkbutton1 - "1080p"
        media_pictures = tk.Checkbutton(root, text="1080p", fg="#2e465e", bg="#15202B",
                                        font=("Comic Sans MS", 13), variable=choice_pictures)
        media_pictures.place(x=30, y=165)

        # Checkbutton2 - "720p"
        media_video = tk.Checkbutton(root, text="720p", fg="#2e465e", bg="#15202B",
                                     font=("Comic Sans MS", 13), variable=choice_videos)
        media_video.place(x=150, y=165)

        # Checkbutton3 - "360p"
        media_stories = tk.Checkbutton(root, text="360p", fg="#2e465e", bg="#15202B",
                                       font=("Comic Sans MS", 13))
        media_stories.place(x=270, y=165)

    def create_start_button(self):
        """================= Creates a start button inside the root window. ================="""
        # Start(download) button
        start_icon = tk.PhotoImage(file='../YoutubeMedia/icons/start.png')
        start_icon_button = tk.Button(root, image=start_icon, bg="#15202B", height="125", width="125",
                                      relief=tk.FLAT, command=lambda: self.press_start_button(acc_input.get()))
        start_icon_button.image = start_icon
        start_icon_button.place(x=132, y=500)
    
    def create_clear_button(self):
        clear_input_button = tk.Button(root, text="Clear",  fg="#000", bg="#2e465e", 
                            borderwidth=1, relief="solid", command=lambda: self.clear_input(self))
        clear_input_button.place(x=270, y=100)
    
    def press_start_button(self,target_url):
        self.run.clean_console()
        self.run.print_text("(Message) Running tests...\n")
        global api_call
        api_call = api.fetchVideo(str(target_url))
        for retry in range(1):
            self.run.print_text("(Message) TEST 1: URL must be valid\n")
            valid = api_call.is_url_valid()
            if valid != False:
                self.run.print_text("(Status) TEST 1: PASSED\n")
                self.run.print_text("(Message) TEST 2: URL must exist on Youtube\n")
                v_title = api_call.get_video_data()
                if v_title != None:
                    self.run.print_text("(Status) TEST 2: PASSED\n\n")
                    self.run.print_text("(Success) Video has been found: \n'"+v_title[:55]+"..'\n\n") 
                    
                    # Call fetch_content function
                    t1=Thread(target=self.print_progressbar(10,10,"\n"))
                    t1.start()
                    api_call.download_video()
                    self.run.print_text("(Success) Successfully downloaded!\n")  
                else:
                    self.run.print_text("(Success) TEST 2: FAILED\n")
                    self.run.print_text("(Error) Video was NOT found on Youtube.\n\n")                 
            if valid != True:
                self.run.print_text("(Status) TEST 1: FAILED\n\n")
                self.run.print_text("(Error) URL is NOT valid\n")
                self.run.print_text("(Message) Please check your link and try again\n")
                break
        return None 

    def print_progressbar(self, count, total, suffix=''):
        bar_len = 40
        filled_len = int(round(bar_len * count / float(total)))
        percents = round(100 * count / float(total), 1)
        bar = '=' * filled_len + '-' * (bar_len - filled_len)
        self.run.print_text("(Status) Downloading the video... \n")
        return self.run.print_text('[%s] %s%s%s\r' % (bar, percents, '', suffix))

    def clear_input(self):
        acc_input.delete(0,END)

    def close_program(self):
        root.destroy()

    def disable_event(self):
        pass
    def click_url(self, url):
        webbrowser.open_new(url)
    
if __name__ == '__main__':
    root = tk.Tk()
    app = Root(root)
    root.mainloop()

