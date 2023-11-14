import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os

def download():
    url = entry_url.get()
    resolution = resolution_var.get()

    progress_label.pack(pady = 10)
    progress_bar.pack(pady = 10)
    status_label.pack(pady = 10)

    try:
        yt = YouTube(url,on_progress_callback=on_progress)
        stream = yt.streams.filter(res=resolution).first()

        os.path.join("C:/Users/hyara/Videos/YT",f"{yt.title}.mp4")
        stream.download(output_path="C:/Users/hyara/Videos/YT")
        status_label.configure(text="Downloaded!", fg_color="green")
    except Exception as e:
        status_label.configure(text= f"Error {str(e)}")

def on_progress(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    completed = bytes_downloaded / total_size * 100
    print(completed)
    progress_label.configure(text=str(int(completed))+ "%")
    progress_label.update()

    progress_bar.set(float(completed/100))


root = ctk.CTk()

ctk.set_appearance_mode("System")

ctk.set_default_color_theme("blue")


root.title("YouTube Downloader!")

# set min and max width and the height

root.geometry("720x480")

root.minsize(720, 480)

root.maxsize(1000, 720)

# create a frame to hold the content
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

url_label = ctk.CTkLabel(content_frame, text="Enter the youtube video URL here :")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady = 10)
entry_url.pack(pady = 10)

#create a download button

download_button = ctk. CTkButton(content_frame, text="Download",command=download)
download_button.pack(pady = 10)

resolutioins = ["1080p","720p", "480p","360p","240p"]
resolution_var = ctk.StringVar()
resolution_combobox = ttk.Combobox (content_frame, values=resolutioins, textvariable=resolution_var)
resolution_combobox.pack(pady = 10)
resolution_combobox.set("1080p")

progress_label = ctk.CTkLabel(content_frame,text= "0%")


progress_bar = ctk.CTkProgressBar(content_frame,width=300)
progress_bar.set(0.1)

status_label = ctk.CTkLabel(content_frame,text="Downloaded")

root.mainloop()