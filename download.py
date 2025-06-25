import os
import uuid
import subprocess
import glob
from yt_dlp import YoutubeDL


def download_video(url, output_dir="downloads"):
    os.makedirs(output_dir, exist_ok=True)
    unique_id = str(uuid.uuid4())
    outtmpl = os.path.join(output_dir, f"{unique_id}.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": outtmpl,
        "quiet": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            raise RuntimeError(f"Failed to download video: {e}")

    files = glob.glob(os.path.join(output_dir, f"{unique_id}.*"))
    if not files:
        raise RuntimeError("Downloaded file not found.")
    return files[0]

def extract_audio(video_path, output_dir="downloads"):
    base = os.path.splitext(os.path.basename(video_path))[0]
    audio_path = os.path.join(output_dir, f"{base}.wav")
    command = [
        "ffmpeg", "-i", video_path, "-ar", "16000", "-ac", "1",
        "-vn", audio_path, "-y", "-loglevel", "quiet"
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to extract audio: {e}")

    return audio_path

def download_and_extract_audio(url):
    video_path = download_video(url)
    audio_path = extract_audio(video_path)
    return audio_path
