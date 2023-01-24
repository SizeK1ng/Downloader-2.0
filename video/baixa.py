import youtube_dl

link = 'https://www.youtube.com/watch?v=YlUKcNNmywk&ab_channel=RedHotChiliPeppers'

opcao = input("Deseja baixar o Video (Sim ou Não)?: ")

ydl_opts = {}
if opcao != 'Sim':
    ydl_opts = {'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
