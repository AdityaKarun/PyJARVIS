# Import core functionalities for voice recognition and speech synthesis
from core.recognizer import recognize_command
from core.speech import speak

# Import various modules for different assistant features
from modules.date_and_time import get_date_time
from modules.greet import greet
from modules.joke import get_joke
from modules.location import get_location
from modules.news import get_news
from modules.search_google import search_google
from modules.weather import get_weather
from modules.youtube_player import youtube_player

# Main entry point of the voice assistant
if __name__ == "__main__":
    # Initialize the assistant with a personalized greeting
    name = "Mister Stark"
    greeting = f"{greet()} {name}!"
    speak(greeting)

    while True:
        command = recognize_command()

        if not command:
            print("Sorry, didn't catch that.")
            continue

        print(command)

        if "sleep" in command or "exit" in command:
            speak("Goodbye Sir!")
            print("Going to Sleep...")
            break

        elif "how are you" in command:
            speak("I am good, thanks for asking. How can I help?")

        elif "time" in command:
            current_time, _, _ = get_date_time()
            speak(f"The current time is {current_time}")

        elif "day" in command:
            _, date, day = get_date_time()
            speak(f"Its {day}, {date}")

        elif "location" in command or "where am i" in command:
            location = get_location()
            speak(f"You are in {location}")

        elif "news" in command or "headlines" in command or "worldwide" in command:
            headlines = get_news()
            speak("Here are the top headlines:")
            for line in headlines:
                speak(line)

        elif "weather" in command or "sky" in command or "conditions" in command:
            weather_report = get_weather()
            speak(f"{weather_report}")

        elif "joke" in command:
            joke = get_joke()
            speak(f"{joke}")

        elif "search" in command or "google" in command:
            query = command.replace("search", "").replace("for", "").replace("google", "").strip()
            speak(f"Searching {query} on Google")
            search_google(query)

        elif "play" in command or "youtube" in command:
            youtube_content = command.replace("play", "").replace("on", "").replace("youtube", "").strip()
            speak(f"Playing {youtube_content} on YouTube")
            youtube_player(youtube_content)

