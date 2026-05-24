#IMPORTANTE 
#Para que o código funcione o primeiro passo é baixar a bilbioteca pytubefix no seu terminal
#Utilizando o comando "pip install pytubefix"

#esse código importa a biblioteca.
from pytubefix import YouTube
#coloca uma barra de progresso do download:
from pytubefix.cli import on_progress 

#codigo para pegar a url do vídeo e colocar na pasta downloads 
url = input("Coloque o URL do vídeo do YouTube: ")
yt = YouTube(url, on_progress_callback=on_progress)
#IMPORTANTE: 
#Quando colar o código mude "USUARIO" pelo usuário que esta logado no seu computador.
yt.streams.get_highest_resolution().download(output_path="C:/Users/USUARIO/Downloads")

print("Download concluído!")
