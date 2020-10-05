from pytube import YouTube

link = input("Enter link of Youtube video:")

yt = YouTube(link)

videos = yt.streams.all()

i = 1

for stream in videos:
    print(str(i)+" "+str(stream))
    i = i+1

stream_num = int(input("Enter number: "))

video = videos[stream_num-1]

video.download("/home/arif/Desktop")

print("Video Downloaded")
