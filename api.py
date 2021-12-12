#!/usr/bin/python3
# YoutubeMedia
# version 1.0
# https://github.com/ruslansco/YoutubeMedia
# Start Date: 12/10/2021
# Rev Date: -

from pytube import YouTube
from pytube import exceptions
import validators
import os
from pytube.cli import on_progress

class fetchVideo:
    """================= Class is responsible for recieving input from URL widget and downloading a video from Youtube. ================="""
    def __init__(self, given_input):
        self.given_input = given_input
        
    def is_url_valid(self):
            if validators.url(self.given_input) != True:
                #print("URL is NOT valid!")
                return False
            else:
                #print("URL is valid!")
                return True

    def get_file_path(self):
        return os.path.join(os.path.expanduser('~'), 'Downloads\YouTubeMedia')

    def get_video_data(self):
        try:
            title = YouTube(self.given_input).title
        except exceptions.RegexMatchError:
                #print("exceptions.RegexMatchError")
                return None
        return title
    
    def download_video(self):
        return YouTube(self.given_input, on_progress_callback=on_progress).streams[1].download(self.get_file_path())
