"""
Text to Speech Module
Author: Person 3
Purpose: Converts text responses to spoken audio (offline)
"""

import pyttsx3
from config import VOICE_RATE, VOICE_VOLUME


class TextToSpeech:
    """
    Handles text-to-speech conversion using pyttsx3.
    Works completely offline.
    """
    
    def __init__(self):
        self.engine = pyttsx3.init()
        self._configure_voice()
    
    def _configure_voice(self):
        """
        Configures voice properties.
        """
        # Set speech rate
        self.engine.setProperty('rate', VOICE_RATE)
        
        # Set volume (0.0 to 1.0)
        self.engine.setProperty('volume', VOICE_VOLUME)
        
        # Get available voices and select one
        voices = self.engine.getProperty('voices')
        
        # Try to use a male voice (typically index 0)
        if voices:
            self.engine.setProperty('voice', voices[0].id)
    
    def speak(self, text):
        """
        Converts text to speech and plays it.
        
        Args:
            text: The text to speak
        """
        if not text:
            return
            
        print(f"Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def greet(self):
        """
        Speaks a greeting message.
        """
        self.speak("Hello! I am Jarvis, your desktop assistant. How can I help you?")
    
    def goodbye(self):
        """
        Speaks a farewell message.
        """
        self.speak("Goodbye! Have a great day!")
    
    def acknowledge(self):
        """
        Speaks an acknowledgment.
        """
        self.speak("Yes, I'm listening.")
    
    def error_message(self):
        """
        Speaks an error message.
        """
        self.speak("Sorry, I didn't understand that. Please try again.")
