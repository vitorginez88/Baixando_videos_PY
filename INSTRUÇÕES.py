#primeiro passo é baixa a bilbioteca pytubefix no seu terminal utilizando o "pip install pytubefix"
#para que o código funcione.

#esse código importa a biblioteca.
from pytubefix import YouTube
#coloca uma barra de progresso do download:
from pytubefix.cli import on_progress 

url = input("Coloque o URL do vídeo do YouTube: ")
yt = YouTube(url, on_progress_callback=on_progress)
yt.streams.get_highest_resolution().download(output_path="C:/Users/USUARIO/Downloads")
