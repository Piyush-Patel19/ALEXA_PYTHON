# 🎙️ Voice Assistant Application (Alexa / Jarvis)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![Stars](https://img.shields.io/github/stars/Piyush-Patel19/ALEXA_PYTHON?style=social)
A Python-based voice assistant inspired by **Alexa and Jarvis** that can listen to voice commands and perform tasks like playing music, searching Wikipedia, opening YouTube, and answering questions using AI.

---

## 🚀 Project Overview

This voice assistant uses **speech recognition and AI** to create an interactive assistant experience.
It listens for wake words and executes commands such as music playback, information retrieval, and general conversation.

---

![Tech](https://skillicons.dev/icons?i=python,git,github,vscode)

## ✨ Features

### 🎤 Voice Recognition

* Detects multiple wake words (Alexa, Aleksa, Alexia, etc. – 16 variations)
* Uses Google Speech Recognition for speech-to-text conversion

### 🎵 Music Playback

* Play songs from a built-in music library
* Opens YouTube links for songs
* Supports Hindi and English songs

### ▶️ YouTube Integration

* Voice commands like **"youtube"** or **"open youtube"** open YouTube

### 📚 Wikipedia Search

* Fetches summaries from Wikipedia
* Reads responses aloud

### 🤖 AI Assistant

* Uses OpenAI (via OpenRouter)
* Provides conversational and intelligent responses

### 🔊 Text-to-Speech

* **pyttsx3** for offline TTS
* **gTTS** for high-quality voice output

---

## 📦 Required Dependencies

Install the required libraries:

```bash
pip install speech_recognition pyttsx3 pywhatkit wikipedia-api openai edge-tts gTTS pygame requests
```

---

## ⚙️ Configuration

### 🔑 OpenAI API Key

1. Open `main.py`
2. Locate the `AI()` function
3. Add your OpenRouter API key:

```python
api_key = "YOUR_API_KEY"
```

👉 Get API key: https://openrouter.ai/

---

### 🌐 Internet Connection

Required for:

* Speech recognition
* Wikipedia
* YouTube playback
* AI responses

---

## ▶️ How to Use

```bash
python main.py
```

1. Say the wake word (e.g., **Alexa**)
2. Give commands

---

## 🎯 Available Commands

### ▶️ YouTube

* `youtube`
* `open youtube`

### 🎵 Music

* `play [song name]`

**Available songs**

* Hindi: kesariya, tum hi ho, apna bana le, chaleya, raataan lambiyan
* English: shape of you, blinding lights, perfect, let her go, believer

### 📚 Wikipedia

* `wikipedia [topic]`
* `search wikipedia for [topic]`

Example:

```
wikipedia Albert Einstein
```

### 🤖 General Questions

Ask anything:

```
What is Python programming?
```

---

## 🎵 Music Library Customization

Edit `musicLibrary.py`:

```python
music = {
    "song_name": "https://www.youtube.com/watch?v=...",
}
```

---

## 🎤 Wake Word Customization

Edit `Call_name` list in `main.py`:

```python
Call_name = ["alexa", "jarvis"]
```

---

## 🛠️ Troubleshooting

**Microphone not detected**

* Check connection and permissions

**Speech not recognized**

* Speak clearly
* Reduce background noise
* Check internet

**AI not responding**

* Verify API key
* Check internet

**Audio playback issues**

* Reinstall pygame
* Check system audio

---

## 📁 Project Structure

```
main.py          → Main assistant logic
musicLibrary.py  → Song dictionary
readme.txt       → Documentation
```

---

## 🎓 Author Notes

This project was created for **educational purposes** and demonstrates integration of speech recognition, APIs, and AI to build a functional voice assistant.

For best results:

* Use a good microphone
* Maintain stable internet connection

---

⭐ If you like this project, consider giving it a star!
