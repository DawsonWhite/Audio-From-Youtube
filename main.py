from pytubefix import YouTube
from sys import argv


link = argv[1]
yt = YouTube(link)
print("Title: ", yt.title)
print("Views: ", yt.views)

vd= yt.streams.get_audio_only()
vd.download() #input desired location here surronded by ""