"""
Command Processing Module
Author: Person 4
Purpose: Interprets user commands and determines actions
"""

from datetime import datetime


class CommandProcessor:
    """
    Processes voice commands and determines appropriate actions.
    """
    
    def __init__(self, app_launcher, text_to_speech):
        self.app_launcher = app_launcher
        self.tts = text_to_speech
        
        # Keywords for different command types
        self.open_keywords = ['open', 'launch', 'start', 'run']
        self.time_keywords = ['time', 'clock']
        self.date_keywords = ['date', 'day', 'today']
        self.exit_keywords = ['exit', 'quit', 'bye', 'goodbye', 'stop', 'close jarvis']
        self.help_keywords = ['help', 'what can you do', 'commands']
    
    def process(self, command):
        """
        Processes a voice command and executes appropriate action.
        
        Args:
            command: The text command from speech recognition
            
        Returns:
            bool: False if should exit, True otherwise
        """
        if not command:
            self.tts.error_message()
            return True
        
        command = command.lower().strip()
        
        # Check for exit command
        if self._check_exit(command):
            self.tts.goodbye()
            return False
        
        # Check for time command
        if self._check_time(command):
            self._tell_time()
            return True
        
        # Check for date command
        if self._check_date(command):
            self._tell_date()
            return True
        
        # Check for help command
        if self._check_help(command):
            self._show_help()
            return True
        
        # Check for open application command
        if self._check_open(command):
            self._open_application(command)
            return True
        
        # Unknown command
        self.tts.speak("Sorry, I don't understand that command. Say help for available commands.")
        return True
    
    def _check_exit(self, command):
        """Check if command is an exit command."""
        return any(keyword in command for keyword in self.exit_keywords)
    
    def _check_time(self, command):
        """Check if command is asking for time."""
        return any(keyword in command for keyword in self.time_keywords)
    
    def _check_date(self, command):
        """Check if command is asking for date."""
        return any(keyword in command for keyword in self.date_keywords)
    
    def _check_help(self, command):
        """Check if command is asking for help."""
        return any(keyword in command for keyword in self.help_keywords)
    
    def _check_open(self, command):
        """Check if command is to open an application."""
        return any(keyword in command for keyword in self.open_keywords)
    
    def _tell_time(self):
        """Tells the current time."""
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        
        # Convert to 12-hour format
        period = "AM" if hour < 12 else "PM"
        hour_12 = hour % 12
        if hour_12 == 0:
            hour_12 = 12
        
        time_str = f"The current time is {hour_12}:{minute:02d} {period}"
        self.tts.speak(time_str)
    
    def _tell_date(self):
        """Tells the current date."""
        now = datetime.now()
        date_str = now.strftime("Today is %A, %B %d, %Y")
        self.tts.speak(date_str)
    
    def _show_help(self):
        """Shows available commands."""
        help_text = """
        I can help you with the following:
        Say 'open' followed by an application name to launch it.
        Say 'what time is it' to know the current time.
        Say 'what is the date' to know today's date.
        Say 'goodbye' to exit.
        """
        self.tts.speak(help_text)
    
    def _open_application(self, command):
        """Extracts app name and opens it."""
        # Remove open keywords from command
        app_name = command
        for keyword in self.open_keywords:
            app_name = app_name.replace(keyword, '')
        
        app_name = app_name.strip()
        
        if app_name:
            success = self.app_launcher.launch(app_name)
            if success:
                self.tts.speak(f"Opening {app_name}")
            else:
                self.tts.speak(f"Sorry, I couldn't find {app_name}")
        else:
            self.tts.speak("Please specify which application to open")
