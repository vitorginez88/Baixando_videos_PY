#IMPORTANTE 
#Para que o código funcione o primeiro passo é baixar a bilbioteca pytubefix no seu terminal
#Utilizando o comando "pip install pytubefix"

#esse código importa a biblioteca:
from pytubefix import YouTube
#coloca uma barra de progresso do download:
from pytubefix.cli import on_progress 

#codigo para pegar a url do vídeo:
url = input("Coloque o URL do vídeo do YouTube: ")
#Escolhe a maior resolução disponível e baixa o vídeo:
yt = YouTube(url, on_progress_callback=on_progress)

#IMPORTANTE: 
#Quando colar o código mude "COLOCAR_DESTINO" por onde você vai querer salvar o vídeo.
yt.streams.get_highest_resolution().download(output_path="COLOCAR_DESTINO")

print("Download concluído!")

#faz com que programa não feche caso o link esteja errado:
except Exception as erro:
    print("Ocorreu um erro:", erro)
