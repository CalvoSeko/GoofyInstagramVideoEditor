import instaloader
import os

def download_instagram_stories(url, output_dir):
    username = extract_username_from_url(url)
    L = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(L.context, username)
        os.makedirs(output_dir, exist_ok=True)

        for story in L.get_stories([profile.userid]):
            for item in story.get_items():
                # Generate a filename based on the item's date
                timestamp = item.date_utc.strftime("%Y-%m-%d_%H-%M-%S_UTC")
                file_extension = "mp4" if item.is_video else "jpg"
                filename = f"{timestamp}.{file_extension}"
                
                # Construct the full file path
                file_path = os.path.join(output_dir, filename)
                
                # Download the item
                L.download_storyitem(item, target=output_dir)
                
                # Find the downloaded file and rename it
                for file in os.listdir(output_dir):
                    if file.startswith(str(item.mediaid)):
                        old_file_path = os.path.join(output_dir, file)
                        os.rename(old_file_path, file_path)
                        print(f"Downloaded story from {username}: {filename}")
                        break
                else:
                    print(f"File not found for media ID: {item.mediaid}")

        print(f"Finished downloading stories for {username}")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"The profile {username} does not exist.")
    except instaloader.exceptions.LoginRequiredException:
        print("Login required. Please uncomment the login line and provide your credentials.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def extract_username_from_url(url):
    # Remove trailing slash if present
    url = url.rstrip('/')
    # Extract the username from the URL
    return url.split('/')[-1]

def download_instagram_stories(url, output_dir):
    # Extract username from URL
    username = extract_username_from_url(url)
    
    # Create an instance of Instaloader
    L = instaloader.Instaloader()

    try:
        # Attempt to login (optional, but allows access to private accounts you follow)
        L.login("abuse.69", "Lu63853830")

        # Get the profile of the user
        profile = instaloader.Profile.from_username(L.context, username)

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Download stories
        for story in L.get_stories([profile.userid]):
            for item in story.get_items():
                # Check if the item is a video
                if item.is_video:
                    # Download the video
                    L.download_storyitem(item, target=output_dir)
                    print(f"Downloaded story from {username}: {item.filename}")

        print(f"Finished downloading stories for {username}")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"The profile {username} does not exist.")
    except instaloader.exceptions.LoginRequiredException:
        print("Login required. Please uncomment the login line and provide your credentials.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    target_url = input("Enter the Instagram profile URL: ")
    output_directory = "instagram_stories"  # Replace with your desired output directory
    download_instagram_stories(target_url, output_directory)