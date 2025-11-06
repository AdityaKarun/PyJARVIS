# Import text-to-speech engine
import pyttsx3

def speak(text):
    """
    Converts text to speech using pyttsx3 engine.
    
    Args:
        text (str): The text to be converted to speech
    """
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    # Set the speaking rate (words per minute)
    engine.setProperty('rate', 200)
    # Print the text for visual feedback
    print(text)
    # Convert text to speech
    engine.say(text)
    # Wait for the speech to complete
    engine.runAndWait()
    # Stop the engine to free up resources
    engine.stop()

if __name__ == "__main__":
    phrase = input("Enter phrase: ")
    speak(phrase)