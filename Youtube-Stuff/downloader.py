from pytube import YouTube
import sys
from colorama import init, Fore

init(autoreset=True) #Colorama initialised

print(Fore.RED + "Enter the URL:", end=' ')
url = input()

try:
    yt = YouTube(url)
except Exception as e:
    print(f"Failed to access video: {e}")
    sys.exit()

video_streams = yt.streams.filter(progressive=True)
audio_streams = yt.streams.filter(only_audio=True)

print("\nAvailable video qualities:")
for stream in video_streams:
    print(f"{stream.itag}: {stream.resolution} - {stream.mime_type}")

print("\nAvailable audio qualities:")
for stream in audio_streams:
    print(f"{stream.itag}: {stream.abr} - {stream.mime_type}")

stream_type = input("\nWould you like to download video or audio? (Enter 'v' or 'a'): ").strip().lower()
itag_choice = input("Enter the itag of the quality you want to download: ")

if stream_type in ["v", "video"]:
    chosen_stream = video_streams.get_by_itag(itag_choice)
elif stream_type in ["a", "audio"]:
    chosen_stream = audio_streams.get_by_itag(itag_choice)
else:
    print("Invalid choice for stream type.")

if chosen_stream: 
    chosen_stream.download('/path/to/save')  #Replace with your path
    print(f"Downloaded: {chosen_stream.resolution if stream_type in ["v", "video"] else chosen_stream.abr} {stream_type}")
else:
    print("Invalid itag selected.")

