import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo, showerror
from pytube import YouTube

def download_media():
    link = link_entry.get()
    try:
        yt = YouTube(link)
        if format_choice.get() == "MP4":
            stream = yt.streams.get_highest_resolution()
            extension = "mp4"
        elif format_choice.get() == "MP3":
            stream = yt.streams.filter(only_audio=True).first()
            extension = "mp3"

        folder_name = 'downloaded_media'
        filename = f"{yt.title}.{extension}"
        file_path = os.path.join(folder_name, filename)
        if os.path.exists(file_path):
            response = messagebox.askquestion("File Exists", f"{filename} already exists. Do you want to overwrite it?")
            if response == "no":
                showinfo("Download Aborted", "Download aborted")
                return

        stream.download(output_path=folder_name, filename=filename)
        showinfo("Download Complete", "Download is completed")
    except Exception as e:
        showerror("Error", f"An error occurred while downloading the media: {e}")

# Create main window
root = tk.Tk()
root.title("Youtube Downloader")
root.geometry("400x200")

# Use a modern theme
style = ttk.Style()
style.theme_use('vista')  # You can choose a different theme if you like

# Create a frame with a cleaner UI
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

label = ttk.Label(frame, text="Enter the link of the video you want to download:")
label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

link_entry = ttk.Entry(frame, width=50)
link_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

format_choice = tk.StringVar(value="MP4")
format_label = ttk.Label(frame, text="Select Download Format:")
format_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

format_menu = ttk.Combobox(frame, textvariable=format_choice, values=["MP4", "MP3"], state="readonly")
format_menu.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

download_button = ttk.Button(frame, text="Download", command=download_media)
download_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()
