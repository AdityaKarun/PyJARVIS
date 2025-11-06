# PyJARVIS - Voice-Controlled Personal Assistant

PyJARVIS is a Python-based voice assistant that helps you with daily tasks, provides information, and controls various functions through voice commands. Inspired by Tony Stark's JARVIS, this assistant can understand voice commands and respond with synthesized speech.

## Features

- 🗣️ **Voice Recognition**: Understands spoken commands using Google's Speech Recognition
- 🔊 **Text-to-Speech**: Responds with natural-sounding voice using pyttsx3
- ⏰ **Time and Date**: Provides current time, date, and day information
- 🌤️ **Weather Updates**: Fetches real-time weather information for your location
- 📰 **News Headlines**: Delivers top headlines from BBC News
- 😄 **Jokes**: Tells programming-related jokes
- 🌍 **Location Detection**: Determines your current city
- 🔍 **Google Search**: Performs web searches directly
- 🎵 **YouTube Control**: Plays videos on YouTube

## Prerequisites

- Python 3.x
- Required Python packages (install using `pip install -r requirements.txt`):
  - pyttsx3
  - pyjokes
  - requests
  - python-dotenv
  - newsapi-python
  - SpeechRecognition
  - PyAudio
  - pywhatkit

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AdityaKarun/PyJARVIS.git
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your API keys:
   ```
   NEWS_API_KEY = your_news_api_key
   WEATHER_API_KEY = your_weather_api_key
   ```

## Usage

1. Run the main script:
   ```bash
   python main.py
   ```

2. Wait for the greeting and then speak your commands.

## Available Commands

- "What time is it?" - Get current time
- "What day is it?" - Get current date and day
- "Where am I?" - Get current location
- "Tell me the news" - Get top news headlines
- "How's the weather?" - Get weather report
- "Tell me a joke" - Hear a programming joke
- "Search for [query]" - Search Google
- "Play [song/video] on YouTube" - Play YouTube content
- "Sleep" or "Exit" - End the program

## Project Structure

```
PyJARVIS/
├── core/
│   ├── recognizer.py  # Speech recognition functionality
│   └── speech.py      # Text-to-speech functionality
├── modules/
│   ├── date_and_time.py    # Time and date functions
│   ├── greet.py            # Greeting generation
│   ├── joke.py             # Joke functionality
│   ├── location.py         # Location detection
│   ├── news.py             # News fetching
│   ├── search_google.py    # Google search
│   ├── weather.py          # Weather information
│   └── youtube_player.py   # YouTube playback
├── .env                    # API keys and configurations
├── main.py                 # Main program file
└── requirements.txt        # Python dependencies
```

## API Keys Required

- [NewsAPI](https://newsapi.org/) - For fetching news headlines
- [WeatherAPI](https://www.weatherapi.com/) - For weather information

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by Iron Man's JARVIS
- Uses various open-source libraries and APIs
