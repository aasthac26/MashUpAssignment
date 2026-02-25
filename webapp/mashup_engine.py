import os
import shutil
import yt_dlp
from pydub import AudioSegment

def reset_folder(folder):
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)

def download_audio(singer, count, folder):
    options = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(folder, "%(title)s.%(ext)s"),
        "quiet": True
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        for i in range(count):
            ydl.download([f"ytsearch1:{singer} song"])

def trim_audio(folder, seconds):
    clips = []
    for file in os.listdir(folder):
        if file.endswith((".webm", ".m4a", ".mp3")):
            audio = AudioSegment.from_file(os.path.join(folder, file))
            part = audio[:seconds * 1000]
            out = os.path.join(folder, "clip_" + file + ".mp3")
            part.export(out, format="mp3")
            clips.append(out)
    return clips

def merge_audio(clips, output_file):
    final = AudioSegment.empty()
    for c in clips:
        final += AudioSegment.from_mp3(c)
    final.export(output_file, format="mp3")