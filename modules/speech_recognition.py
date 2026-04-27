"""
Speech Recognition Module
Author: Person 2
Purpose: Converts spoken commands to text (offline)
"""

import speech_recognition as sr
from config import RECOGNITION_TIMEOUT, PHRASE_TIME_LIMIT


class SpeechRecognizer:
    """
    Handles speech-to-text conversion using offline recognition.
    """
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Configure recognizer
        self.recognizer.energy_threshold = 4000
        self.recognizer.dynamic_energy_threshold = True
    
    def listen(self):
        """
        Listens for user speech and converts to text.
        Returns the recognized text or None if not understood.
        """
        print("Listening for command...")
        
        try:
            with self.microphone as source:
                # Brief pause to let user start speaking
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                
                audio = self.recognizer.listen(
                    source,
                    timeout=RECOGNITION_TIMEOUT,
                    phrase_time_limit=PHRASE_TIME_LIMIT
                )
            
            # Use offline Sphinx recognition
            text = self.recognizer.recognize_sphinx(audio)
            print(f"Recognized: {text}")
            return text.lower().strip()
            
        except sr.WaitTimeoutError:
            print("No speech detected (timeout)")
            return None
            
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
            
        except sr.RequestError as e:
            print(f"Recognition error: {e}")
            return None
            
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
    
    def get_command(self):
        """
        Gets a single command from the user.
        Retries once if first attempt fails.
        """
        text = self.listen()
        
        if text is None:
            print("Please try again...")
            text = self.listen()
            
        return text
