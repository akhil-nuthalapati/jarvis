import speech_recognition as sr
from config import SPEECH


class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        # One-time calibration
        with self.microphone as source:
            print("Calibrating microphone...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

    def listen(self):
        try:
            with self.microphone as source:
                audio = self.recognizer.listen(
                    source,
                    timeout=SPEECH["timeout"],
                    phrase_time_limit=SPEECH["phrase_limit"]
                )

            text = self.recognizer.recognize_sphinx(audio)
            return text.lower().strip()

        except (sr.WaitTimeoutError, sr.UnknownValueError):
            return None
        except Exception as e:
            print(f"Speech error: {e}")
            return None