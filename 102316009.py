import sys
import os
import shutil
import yt_dlp
from pydub import AudioSegment

# -----------------------------
# Helper: Create Fresh Directory
# -----------------------------
def prepare_directory(folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)
    os.makedirs(folder_name)
# -----------------------------
# Step 1: Download Audio from YouTube
# -----------------------------
def fetch_audio_tracks(artist_name, total_videos, download_path):
    print("\nSearching and downloading audio tracks...\n")

    ydl_options = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(download_path, "%(title)s.%(ext)s"),
        "quiet": True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_options) as downloader:
            for index in range(total_videos):
                search_query = f"ytsearch1:{artist_name} official song"
                downloader.download([search_query])
                print(f"Downloaded file {index + 1}/{total_videos}")
    except Exception as error:
        print("Error during downloading:", error)
        sys.exit(1)


# -----------------------------
# Step 2: Trim Audio Files
# -----------------------------
def trim_tracks(download_path, duration_seconds):
    print("\nTrimming audio files...\n")

    trimmed_files = []

    try:
        for file in os.listdir(download_path):
            file_path = os.path.join(download_path, file)

            if file.endswith((".webm", ".m4a", ".mp3")):
                audio = AudioSegment.from_file(file_path)
                clipped_audio = audio[: duration_seconds * 1000]

                output_name = "clip_" + file + ".mp3"
                output_path = os.path.join(download_path, output_name)

                clipped_audio.export(output_path, format="mp3")
                trimmed_files.append(output_path)

        return trimmed_files

    except Exception as error:
        print("Error while trimming:", error)
        sys.exit(1)


# -----------------------------
# Step 3: Merge All Clips
# -----------------------------
def create_mashup(audio_clips, final_output_name):
    print("\nMerging clips into final mashup...\n")

    try:
        combined_audio = AudioSegment.empty()

        for clip in audio_clips:
            sound = AudioSegment.from_mp3(clip)
            combined_audio += sound

        combined_audio.export(final_output_name, format="mp3")
        print("\nMashup successfully created:", final_output_name)

    except Exception as error:
        print("Error during merging:", error)
        sys.exit(1)


# -----------------------------
# Main Execution Block
# -----------------------------
def main():

    if len(sys.argv) != 5:
        print("\nUsage:")
        print("python <RollNumber>.py <SingerName> <NumberOfVideos> <DurationInSeconds> <OutputFileName>\n")
        sys.exit(1)

    singer_name = sys.argv[1]

    try:
        video_count = int(sys.argv[2])
        clip_duration = int(sys.argv[3])
    except ValueError:
        print("NumberOfVideos and Duration must be integers.")
        sys.exit(1)

    output_file = sys.argv[4]

    # Assignment constraints
    if video_count <= 10:
        print("NumberOfVideos must be greater than 10.")
        sys.exit(1)

    if clip_duration <= 20:
        print("Duration must be greater than 20 seconds.")
        sys.exit(1)

    download_folder = "temp_downloads"

    prepare_directory(download_folder)

    fetch_audio_tracks(singer_name, video_count, download_folder)

    clips = trim_tracks(download_folder, clip_duration)

    create_mashup(clips, output_file)

    print("\nProcess completed successfully.\n")


if __name__ == "__main__":
    main()