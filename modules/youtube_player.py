# Import pywhatkit for YouTube playback functionality
import pywhatkit

def youtube_player(content):
    """
    Opens a web browser and plays the requested content on YouTube.
    
    Args:
        content (str): The search term or video title to play on YouTube
    """
    pywhatkit.playonyt(content)

if __name__ == "__main__":
    content = input("Search YouTube: ")
    print(f"Playing {content} on YouTube.")
    youtube_player(content)