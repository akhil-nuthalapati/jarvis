"""
Configuration settings for Jarvis Assistant
"""

# Wake word to activate Jarvis
WAKE_WORD = "jarvis"

# Speech recognition settings
RECOGNITION_TIMEOUT = 5
PHRASE_TIME_LIMIT = 8

# Text-to-speech settings
VOICE_RATE = 150
VOICE_VOLUME = 1.0

# Application paths (customize for your system)
# Windows examples - modify paths as needed
APPLICATIONS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "firefox": r"C:\Program Files\Mozilla Firefox\firefox.exe",
    "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    "explorer": "explorer.exe",
    "cmd": "cmd.exe",
    "paint": "mspaint.exe",
    "snipping tool": "snippingtool.exe",
    "task manager": "taskmgr.exe",
    "control panel": "control.exe",
    "settings": "ms-settings:",
}

# Linux/Mac alternatives (uncomment if needed)
# APPLICATIONS = {
#     "terminal": "gnome-terminal",
#     "firefox": "firefox",
#     "files": "nautilus",
#     "calculator": "gnome-calculator",
#     "text editor": "gedit",
# }
