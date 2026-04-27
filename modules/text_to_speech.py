import pyttsx3
from config import VOICE


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()

        # Configure voice
        self.engine.setProperty("rate", VOICE["rate"])
        self.engine.setProperty("volume", VOICE["volume"])

        voices = self.engine.getProperty("voices")
        if voices:
            self.engine.setProperty("voice", voices[0].id)

    def speak(self, text):
        if not text:
            return

        print(f"Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()