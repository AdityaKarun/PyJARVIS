# Import the speech recognition library for voice input processing
import speech_recognition

def recognize_command():
    """
    Listens to user's voice input and converts it to text using Google's speech recognition.
    
    Returns:
        str: The recognized command in lowercase, or None if recognition fails
    """
    # Initialize the speech recognizer
    recognizer = speech_recognition.Recognizer()

    # Use the microphone as audio source
    with speech_recognition.Microphone() as source:
        print("Listening...")
        # Adjust for ambient noise to improve recognition accuracy
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        # Listen for user's voice input
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        command = command.lower()
        return command

    except Exception as e:
        print(f"Recognition error: {e}")
        return None

if __name__ == "__main__":
    input("Hit enter to start voice recognition.")
    command = recognize_command()
    print(command)
