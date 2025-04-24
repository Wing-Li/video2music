# utils.py - 工具和通用功能
import eel
import tkinter as tk
from tkinter import filedialog

@eel.expose
def select_directory():
    """打开文件夹选择对话框"""
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory()
    root.destroy()
    return directory

@eel.expose
def select_file(filetypes=None):
    """打开文件选择对话框"""
    if filetypes is None:
        filetypes = [
            ("音频文件", "*.mp3 *.wav *.ogg *.flac"), 
            ("视频文件", "*.mp4 *.avi *.mov *.mkv *.flv *.wmv *.webm"),
            ("所有文件", "*.*")
        ]
    
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=filetypes)
    root.destroy()
    return file_path 