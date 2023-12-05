import youtube_dl

def download_youtube_video_as_mp3(youtube_url):
  # Get the highest quality audio stream from the YouTube video.
  yt_video = youtube_dl.YoutubeDL().extract_info(
    url=youtube_url,
    format="bestaudio",
    # This option will convert the audio to MP3 format.
    output_format="mp3"
  )

  # Get the filename of the MP3 file.
  filename = f"{yt_video['title']}.mp3"

  # Download the MP3 file to the current directory.
  with youtube_dl.YoutubeDL(params={"outtmpl": filename}) as ydl:
    ydl.download([youtube_url])

if __name__ == "__main__":
  # Get the YouTube video URL from the user.
  youtube_url = input("Enter the YouTube video URL: ")

  # Download the YouTube video as an MP3 file.
  download_youtube_video_as_mp3(youtube_url)

  print(f"The YouTube video has been downloaded as {filename}.")
