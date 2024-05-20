import pytube

link = input('Youtube URL: ')
video = pytube.YouTube(link)
video.streams.first().download()

print('Video downloaded', link)