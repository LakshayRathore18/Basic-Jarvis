import speech_recognition as sr
import pyttsx3
from speaknlisten import speak,listen
from command import process_command

# Initialize recognizer & TTS engine once
recognizer = sr.Recognizer()
engine = pyttsx3.init()


if __name__ == "__main__":
    speak("Jarvis at your service.")
    while True:
        cmd = listen()
        if "jarvis" in cmd:
            # strip the wake word and leading spaces
            cmd = cmd.replace("jarvis", "").strip()
            if not process_command(cmd):
                break