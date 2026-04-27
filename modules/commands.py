from datetime import datetime


class CommandProcessor:
    def __init__(self, app_launcher, tts):
        self.apps = app_launcher
        self.tts = tts

    def process(self, command):
        if not command:
            self.tts.speak("I didn't catch that")
            return True

        command = command.lower().strip()

        # Exit
        if any(x in command for x in ["exit", "quit", "bye", "stop"]):
            self.tts.speak("Goodbye")
            return False

        # Time
        if "time" in command:
            now = datetime.now().strftime("%I:%M %p")
            self.tts.speak(f"The time is {now}")
            return True

        # Date
        if "date" in command or "day" in command:
            today = datetime.now().strftime("%A, %B %d")
            self.tts.speak(f"Today is {today}")
            return True

        # Help
        if "help" in command:
            self.tts.speak(
                "You can say open apps, ask time or date, or say exit to quit."
            )
            return True

        # Open app
        if "open" in command:
            app = command.replace("open", "").strip()

            if not app:
                self.tts.speak("Which app?")
                return True

            if self.apps.launch(app):
                self.tts.speak(f"Opening {app}")
            else:
                self.tts.speak(f"I couldn't find {app}")

            return True

        # Unknown
        self.tts.speak("Unknown command")
        return True