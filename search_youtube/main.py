from pytube import YouTube
import ssl
import subprocess

ssl._create_default_https_context = ssl._create_stdlib_context

def get_youtube_video(link):
    youtube = YouTube(link)
    video = youtube.streams.get_highest_resolution()
    print(video)
    return video

def download_video(link):
    yt_video = get_youtube_video(link)
    file_path = yt_video.download(output_path='/Users/owenfeng/Documents/search-youtube')
    print('Download complete!')
    print(file_path)
    return file_path

def convert_to_mp3(input_file, output_file='audio.mp3'):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "192k",
        "-ar", "44100",
        "-y", output_file
    ]
    try: 
        subprocess.run(ffmpeg_cmd, check=True)
        print('Converted!')
    except subprocess.CalledProcessError as e:
        print('Conversion failed:', e)

user_link = input('Give me your link 😩:')
downloaded_file_path = download_video(user_link) 
convert_to_mp3(downloaded_file_path)