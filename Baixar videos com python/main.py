from pytubefix import YouTube
from pytubefix.cli import on_progress 

url = input("Coloque o URL do vídeo do YouTube: ")
yt = YouTube(url, on_progress_callback=on_progress)
yt.streams.get_highest_resolution().download(output_path="C:/Users/USUARIO/Downloads")


