"""
Wake Word Detection Module
Author: Person 1
Purpose: Detects when user says the wake word "Jarvis"
"""

import speech_recognition as sr
from config import WAKE_WORD


class WakeWordDetector:
    """
    Listens for the wake word to activate Jarvis.
    Uses offline speech recognition.
    """
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.wake_word = WAKE_WORD.lower()
        
        # Adjust for ambient noise on initialization
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
    
    def listen_for_wake_word(self):
        """
        Continuously listens for the wake word.
        Returns True when wake word is detected.
        """
        print(f"Listening for wake word '{self.wake_word}'...")
        
        try:
            with self.microphone as source:
                audio = self.recognizer.listen(source, timeout=None, phrase_time_limit=3)
            
            # Use offline recognition (Sphinx)
            try:
                text = self.recognizer.recognize_sphinx(audio).lower()
                print(f"Heard: {text}")
                
                if self.wake_word in text:
                    return True
                    
            except sr.UnknownValueError:
                # Speech not understood, continue listening
                pass
                
        except sr.WaitTimeoutError:
            pass
        except Exception as e:
            print(f"Wake word detection error: {e}")
            
        return False
    
    def wait_for_activation(self):
        """
        Blocks until wake word is detected.
        """
        while True:
            if self.listen_for_wake_word():
                return True
