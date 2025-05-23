import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text: str):
    engine.say(text)
    engine.runAndWait()

def listen() -> str:
    with sr.Microphone() as source:
        print("🎙 Listening...")
        audio = recognizer.listen(source)
    try:
        cmd = recognizer.recognize_google(audio).lower()
        print("🗣 You said:", cmd)
        return cmd
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the service.")
        return ""
