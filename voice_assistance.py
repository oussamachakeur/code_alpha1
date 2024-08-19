import speech_recognition as sp
import datetime
import pyttsx3
import webbrowser
import openai
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


openai.api_key = 'your-api-key-here'  # Replace with your actual API key

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Initialize the recognizer
recognizer = sp.Recognizer()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for voice input and return it as text."""
    with sp.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sp.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
            return ""
        except sp.RequestError:
            print("Sorry, there is an issue with the service.")
            speak("Sorry, there is an issue with the service.")
            return ""

def tell_time():
    """Tell the current time."""
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"The time is {current_time}")

def open_website(url):
    """Open a website."""
    webbrowser.open(url)
    speak("as you want boss")
    


def main():
    """Main function to run the voice assistant."""
    speak("Hello oussama! How can I assist you today?")
    
    while True:
        command = listen()
        
        if 'time' in command:
            tell_time()   
        elif 'open google' in command:
            open_website('https://www.google.com')
        elif 'open youtube' in command:
            open_website('https://www.youtube.com')
        elif 'open my email box' in command:
            open_website('https://mail.google.com')   
        elif 'open my whatsapp' in command:
            open_website('https://web.whatsapp.com')     
        elif "thank you" in command:
            speak("you are welcome oussama ,any time")
        elif "what is your name " in command:
            speak("my name is auba")    
        elif 'exit' in command or 'stop' in command:
            speak("Goodbye oussanma!") 
            break
        
        else:
            speak("please repeat")

if __name__ == "__main__":
    main()



