import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from openai import OpenAI
import edge_tts
import asyncio
import os
from gtts import gTTS
import pygame
import time
import urllib.parse
import wikipedia
import wikipediaapi

import requests


Call_name = [
    'alexa',
    'alexaa',
    'alexia',
    'alexsa',
    'alexxa',
    'alexxia',
    'alexsaa',
    'aleksa',
    'aleksa',
    'alexah',
    'alexza',
    'alexus',
    'alexys',
    'alecsa',
    'aleqsa',
    'alekxa'
]

Commands = ["youtube","open youtube","utube"]
engine = pyttsx3.init() # object creation
r = sr.Recognizer()
pygame.mixer.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def speak_new(text):
    tts = gTTS(text=text, lang="en",slow=False)
    tts.save("jarvis.mp3")
    
    pygame.mixer.music.load("jarvis.mp3")
    pygame.mixer.music.play()

    # Wait until audio finishes playing
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.music.unload()
    os.remove("jarvis.mp3")

def AI(Command):
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="",
    )
    try:
        response = client.chat.completions.create(
        model="arcee-ai/trinity-large-preview:free",
        messages=[
                 {
                    "role": "system",
                    "content": "You are Jarvis, a smart AI assistant. Give short, direct answers in 1-3 sentences. Do not use bullet points, formatting, or explanations unless asked."
                },
                 
                {"role": "user", "content": Command}
            ]
        )
    except Exception as e:
           print("AI Error:", e)
           return "Sorry, I am having trouble connecting."
 
    # Extract the assistant message with reasoning_details
    return response.choices[0].message.content
## Wiki Pedia 
def wiki(Command): 
        summary = wikipedia.summary(Command, sentences=2)
        return summary
def imagegeneration(Command):
    prompt = Command
    url = f"https://gen.pollinations.ai/image/{(prompt)}"
    img_data = requests.get(url).content
    with open("robot_mural.jpg","wb") as f:
        f.write(img_data)
    print("Image saved!")   
def process_command(command):
    if command.lower() in Commands:
        webbrowser.open("https://youtube.com")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        musicLink = musicLibrary.music[song]
        webbrowser.open(musicLink)
    # elif  "play" in command or "youtube" in command:
    #     speak_new("Searching on YouTube")
    #     search_query = command.replace("play", "").replace("youtube", "").strip()
    #     youtube_url = f"https://www.youtube.com/results?search_query={search_query}"
    #     webbrowser.open(youtube_url)
    # elif "Wikipedia" or "search from wikipedia":
    #     speak_new("Searching On Wikipedia")
    #     search_query = command.replace("Wikipedia", "").replace("search from wikipedia", "").replace("from","").strip()
    #     wiki_output = wiki(search_query)
    #     print(wiki_output)
    #     speak_new(wiki_output)
    elif "wikipedia" in command.lower():
        speak_new("Searching on Wikipedia")                                                                
        clean_command = command.lower()
        clean_command = re.sub(r"(search|from|on|wikipedia|tell me about|what is)", "", clean_command)
        search_query = clean_command.strip()
        wiki_output = wiki(search_query)
        print("Wiki:", wiki_output)
        speak_new(wiki_output)  
    else:
        AI_output = AI(command)
        print(AI_output)
        speak_new(AI_output)

    
if __name__=="__main__":
        while True:
            try:
                with sr.Microphone() as source:
                    print("Say something!")
                    audio = r.listen(source)
                    Word = r.recognize_google(audio)
                if(Word.lower() in Call_name ):
                    speak_new("Alexa Here")
                    print("Alexa Here")
                    with sr.Microphone() as source:
                        audio = r.listen(source, timeout=None)
                        Command = r.recognize_google(audio)
                    print(Command)
                    process_command(Command)
            except sr.UnknownValueError:
                print("Google Cloud Speech could not understand audio")
            except sr.RequestError as e:
             print("Could not request results from Google Cloud Speech service; {0}".format(e))

    
