import os
import yt_dlp

def download_video(url, input='input'):
    # Create the output folder if it doesn't exist
    os.makedirs(input, exist_ok=True)

    # Configure yt-dlp options
    ydl_opts = {
        'outtmpl': os.path.join(input, '%(title)s.%(ext)s'),
        'format': 'best',
    }

    # Create a yt-dlp object and download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print(f"Video downloaded successfully to {input}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

def main():
    while True:
        url = input("Enter the video URL (or 'q' to quit): ")
        if url.lower() == 'q':
            break
        
        output_folder = input("Enter the output folder name (press Enter for default 'input'): ")
        if not output_folder:
            output_folder = 'input'
        
        download_video(url, output_folder)
        print()  # Add a blank line for better readability

if __name__ == "__main__":
    main()

download_video("https://www.instagram.com/stories/alviseperez/")
# Example usage
# download_video('https://www.instagram.com/reel/abcdefghijk/')
# download_video('https://www.youtube.