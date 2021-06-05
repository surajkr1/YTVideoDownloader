import pytube
from pytube import YouTube
 

url = "link"
path = "path to save downloaded video"

try:
        link = pytube.YouTube(url)
        print("Connection Success")
except:
        print("Connection Error")

dvid = link.streams.get_by_resolution('720p')
dvid.download(path)
print("Complete Download")