class JarvisAssistant:
    def __init__(self):
        self.tts = TextToSpeech()
        self.recognizer = SpeechRecognizer()
        self.apps = AppLauncher()

    def run(self):
        self.tts.speak("Jarvis ready")

        while True:
            try:
                text = self.recognizer.listen()

                if not text:
                    continue

                if "jarvis" in text:
                    self.tts.speak("Yes?")
                    command = self.recognizer.listen()
                    self.handle_command(command)

            except KeyboardInterrupt:
                self.tts.speak("Goodbye")
                break

    def handle_command(self, command):
        if not command:
            self.tts.speak("Say that again")
            return

        command = command.lower()

        if any(x in command for x in ["exit", "quit", "bye"]):
            self.tts.speak("Goodbye")
            exit()

        elif "time" in command:
            from datetime import datetime
            self.tts.speak(datetime.now().strftime("%I:%M %p"))

        elif "date" in command:
            from datetime import datetime
            self.tts.speak(datetime.now().strftime("%A, %B %d"))

        elif "open" in command:
            app = command.replace("open", "").strip()
            if self.apps.launch(app):
                self.tts.speak(f"Opening {app}")
            else:
                self.tts.speak("App not found")

        else:
            self.tts.speak("Unknown command")