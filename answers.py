import os
import requests
from urllib.parse import urlparse

def fetch_image():
    # Prompt user for an image URL
    url = input("Enter the URL of the image you want to fetch: ").strip()

    # Create directory "Fetched_Images" if it doesn't exist
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Send HTTP request to fetch the image
        response = requests.get(url, stream=True)
        response.raise_for_status()  

        # Extract filename from the URL, fallback to a default
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:  
            filename = "downloaded_image.jpg" 

        # Full path to save the image
        file_path = os.path.join(save_dir, filename)

        # Save image in binary mode
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"Image successfully fetched and saved as: {file_path}")

    except requests.exceptions.MissingSchema:
        print("Invalid URL. Please enter a proper image URL (including http/https).")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests.exceptions.ConnectionError:
        print("Connection error. Please check your internet connection.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("The Wisdom of Ubuntu: 'I am because we are'")
    fetch_image()
