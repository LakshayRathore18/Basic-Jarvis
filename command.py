import speech_recognition as sr
import webbrowser
import pyttsx3
import pywhatkit

from gemini import generate_ai_content
from speaknlisten import speak

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def handle_open_website(cmd: str):
    if "youtube" in cmd:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "google" in cmd:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

def handle_play_song(cmd: str):
    song = cmd.replace("play", "").strip()
    if song:
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)
    else:
        speak("Please say the name of the song after 'play'.")

def handle_gemini_query(cmd: str):
    question = (
        cmd.replace("what is", "")
           .replace("define", "")
           .replace("explain", "")
           .strip()
    )
    if question:
        speak(f"Let me explain {question}")
        answer = generate_ai_content(question)
        print("🤖 Gemini:", answer)
        speak(answer)
    else:
        speak("Please ask a complete question.")

def process_command(cmd: str) -> bool:
    if "open" in cmd:
        handle_open_website(cmd)
    elif cmd.startswith("play "):
        handle_play_song(cmd)
    elif any(kw in cmd for kw in ("what is", "define", "explain")):
        handle_gemini_query(cmd)
    elif any(kw in cmd for kw in ("stop", "exit")):
        speak("Goodbye, sir.")
        return False
    else:
        speak("I didn't get that.")
    return True
