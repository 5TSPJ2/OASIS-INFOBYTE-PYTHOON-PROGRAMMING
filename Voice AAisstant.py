#OASIS-INFOBYTE INTERNSHIP(BEGGINERS)
#TASK1 VOICE ASSISSTANT CREATION

import speech_recognition as sr
import pyttsx3
import datetime
import requests

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        return ""

def respond(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "name" in command:
        speak("Hello! my name is vvassisstant")
   
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")
    elif "date" in command:
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {today}")
    elif "search for" in command:
        search_term = command.replace("search for", "").strip()
        url = f"https://www.google.com/search?q={search_term}"
        speak(f"Here are the search results for {search_term}")
        requests.get(url)  # Simple way to indicate search action
    else:
        speak("Sorry, I didn't get that.")
if __name__ == "__main__":
    speak("Voice assistant is ready.")
    while True:
        command = listen()
        respond(command)














