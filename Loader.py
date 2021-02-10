from pytube import YouTube
link = input("Enter the link of YouTube video you want to download: ")
yt = YouTube(link)
#Title of video
print('Title: ',yt.title)
#Number of views of video
print('Number of views: ',yt.views)
#Length of the video
print('Length of video: ',yt.length,'seconds')
#Description of video
print('Description: ',yt.description)
#Rating
print('Ratings: ',yt.rating)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()
#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")