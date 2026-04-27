"""
Jarvis Desktop Assistant - Main Entry Point
A simple offline voice-controlled desktop assistant.

Usage:
    python main.py
    
Say "Jarvis" to activate, then give a command.
"""

import sys
from modules import (
    WakeWordDetector,
    SpeechRecognizer,
    TextToSpeech,
    CommandProcessor,
    AppLauncher
)


class JarvisAssistant:
    """
    Main Jarvis Assistant class.
    Coordinates all modules to create a voice-controlled assistant.
    """
    
    def __init__(self):
        print("Initializing Jarvis Assistant...")
        print("-" * 40)
        
        # Initialize all modules
        self.tts = TextToSpeech()
        self.wake_detector = WakeWordDetector()
        self.speech_recognizer = SpeechRecognizer()
        self.app_launcher = AppLauncher()
        self.command_processor = CommandProcessor(self.app_launcher, self.tts)
        
        print("All modules initialized successfully!")
        print("-" * 40)
    
    def run(self):
        """
        Main loop for the assistant.
        """
        self.tts.greet()
        
        running = True
        
        while running:
            try:
                # Wait for wake word
                print("\n" + "=" * 40)
                print("Say 'Jarvis' to activate...")
                print("=" * 40)
                
                self.wake_detector.wait_for_activation()
                
                # Acknowledge activation
                self.tts.acknowledge()
                
                # Listen for command
                command = self.speech_recognizer.get_command()
                
                # Process command
                if command:
                    running = self.command_processor.process(command)
                else:
                    self.tts.error_message()
                    
            except KeyboardInterrupt:
                print("\nInterrupted by user")
                self.tts.goodbye()
                running = False
                
            except Exception as e:
                print(f"Error: {e}")
                self.tts.speak("An error occurred. Please try again.")
        
        print("\nJarvis Assistant stopped.")


def main():
    """
    Entry point for the application.
    """
    print("=" * 50)
    print("   JARVIS - Desktop Voice Assistant")
    print("=" * 50)
    print()
    
    try:
        assistant = JarvisAssistant()
        assistant.run()
        
    except Exception as e:
        print(f"Failed to start Jarvis: {e}")
        print("\nMake sure you have installed all requirements:")
        print("  pip install pyttsx3 SpeechRecognition pyaudio")
        print("\nOn Linux, you may also need:")
        print("  sudo apt install python3-pyaudio portaudio19-dev")
        sys.exit(1)


if __name__ == "__main__":
    main()
