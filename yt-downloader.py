import os
import datetime
import subprocess

def get_output_dir():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = os.path.join(os.getcwd(), f"download_{timestamp}/")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        os.chmod(output_dir, 0o755)

    return output_dir

def build_command(url, is_playlist, audio_only):
    output_dir = get_output_dir()
    format_options = "--format bestaudio --extract-audio --audio-format mp3" if audio_only else ""
    playlist_option = "--yes-playlist" if is_playlist else ""
    file = f"{output_dir}%(title)s" if audio_only else f"{output_dir}%(title)s.%(ext)s"
    
    return f'yt-dlp {format_options} {playlist_option} -o {file} {url}'

def run_command(command):
    try:
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, universal_newlines=True)

        for output in process.stdout:
            print(output.strip())

        process.wait()

        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, process.args)
    except Exception as e:
        print(f"Oops! Sorry, an error occurred: {e}. Cannot continue with download.")

if __name__ == "__main__":
    print("\n\n**********************************")
    print("Welcome to the youtube downloader.")
    print("**********************************\n\n")

    url = input("Please enter the YouTube URL you want to download from: ")
    is_playlist = input("Is this a playlist URL? (Yes/No): ").lower() == "yes"
    audio_only = input("Do you want to download the audio only? (Yes/No): ").lower() == "yes"

    command = build_command(url, is_playlist, audio_only)
    run_command(command)
