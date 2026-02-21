================================================================================
                    VOICE ASSISTANT APPLICATION (Alexa/Jarvis)
================================================================================

Project Overview:
-----------------
This is a voice assistant application similar to Alexa or Jarvis. It uses 
speech recognition to listen for voice commands and performs various tasks 
including playing music, searching Wikipedia, and answering 
questions using AI.


Features:
---------
1. Voice Recognition
   - Listens for wake words (alexa, aleksa, alexia, etc. - 16 variations)
   - Uses Google Speech Recognition for converting speech to text

2. Music Playback
   - Play songs from a built-in music library
   - Opens YouTube links for songs
   - Supports both Hindi and English songs

3. YouTube Integration
   - Open YouTube with voice commands like "youtube" or "open youtube"

4. Wikipedia Search
   - Search Wikipedia for information
   - Speaks back the Wikipedia summary

5. AI Assistant
   - Uses OpenAI (via OpenRouter) to answer general questions
   - Provides smart, conversational responses

6. Text-to-Speech
   - Uses pyttsx3 for system TTS
   - Uses gTTS (Google Text-to-Speech) for high-quality voice output



Required Dependencies:
---------------------
Install the following Python libraries:

pip install speech_recognition
pip install pyttsx3
pip install pywhatkit
pip install wikipedia-api
pip install openai
pip install edge-tts
pip install gTTS
pip install pygame
pip install requests


Configuration:
-------------
1. OpenAI API Key:
   - In main.py, find the AI() function
   - Add your OpenRouter API key in the api_key="" field
   - Get your free API key from: https://openrouter.ai/

2. Internet Connection:
   - Required for speech recognition, YouTube, Wikipedia, and AI features


How to Use:
-----------
1. Run the application:
   python main.py

2. Say the wake word to activate (e.g., "Alexa")

3. Available commands:
   
   a) YouTube:
      - "youtube" or "open youtube" - Opens YouTube homepage
   
   b) Music:
      - "play [song name]" - Plays the song from music library
      - Available songs:
        * Hindi: kesariya, tum hi ho, apna bana le, chaleya, raataan lambiyan
        * English: shape of you, blinding lights, perfect, let her go, believer
   
   c) Wikipedia:
      - "wikipedia [topic]" or "search wikipedia for [topic]"
      - Example: "wikipedia Albert Einstein"
   
   
   d) General Questions:
      - Ask anything and AI will answer
      - Example: "What is Python programming?"


Music Library Customization:
----------------------------
Edit musicLibrary.py to add more songs:

music = {
    "song_name": "https://www.youtube.com/watch?v=...",
    # Add more songs here
}


Wake Word Customization:
------------------------
Edit the Call_name list in main.py to add more wake words:

Call_name = [
    'alexa',
    'jarvis',
    # Add more wake words here
]


Troubleshooting:
----------------
1. Microphone not detected:
   - Check if microphone is properly connected
   - Ensure microphone permissions are granted

2. Speech not recognized:
   - Speak clearly and loudly
   - Check internet connection
   - Reduce background noise

3. AI not responding:
   - Verify OpenRouter API key is added
   - Check internet connection

4. Audio playback issues:
   - Ensure pygame is properly installed
   - Check system audio settings


Project Structure:
------------------
- main.py              : Main application file with all functions
- musicLibrary.py      : Dictionary of songs with YouTube links
- readme.txt           : This documentation file


Author Notes:
-------------
This is a voice assistant project created for educational purposes. 
The application uses various APIs and libraries to provide a complete 
voice assistant experience.

For best results, use a good quality microphone and ensure stable 
internet connection.

================================================================================
