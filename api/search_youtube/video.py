import uuid

from pytube import YouTube

from .storage import Storage


def get_youtube_video(link: str):
    youtube = YouTube(link)
    video = youtube.streams.filter(only_audio=True).first()

    return video


def download_youtube_video(link: str, out: str = "./out", as_local_file: bool = False):
    video = get_youtube_video(link)
    output = video.download(output_path=out)

    if as_local_file:
        return output

    storage = Storage("<insert video bucket here>")

    with open(output, "rb") as f:
        id = str(uuid.uuid4())
        ext = output.split(".")[-1]

        response = storage.upload(f"{id}.{ext}", f, "video/mpeg")
        return f"{id}.{ext}"
