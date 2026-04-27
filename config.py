import platform

# --- General ---
WAKE_WORD = "jarvis"

# --- Speech ---
SPEECH = {
    "timeout": 5,
    "phrase_limit": 8
}

# --- Voice ---
VOICE = {
    "rate": 150,
    "volume": 1.0
}

# --- Detect OS ---
SYSTEM = platform.system()

# --- Applications ---
if SYSTEM == "Windows":
    APPLICATIONS = {
        # System Tools
        "notepad": "notepad",
        "calculator": "calc",
        "cmd": "cmd",
        "powershell": "powershell",
        "task manager": "taskmgr",
        "control panel": "control",
        "settings": "ms-settings:",
        "explorer": "explorer",

        # Browsers
        "chrome": "chrome",
        "firefox": "firefox",
        "edge": "msedge",

        # Office
        "word": "winword",
        "excel": "excel",
        "powerpoint": "powerpnt",

        # Media
        "vlc": "vlc",
        "windows media player": "wmplayer",

        # Dev Tools
        "vscode": "code",
        "visual studio": "devenv",
        "git bash": "git-bash",

        # Utilities
        "paint": "mspaint",
        "snipping tool": "snippingtool",
        "camera": "start microsoft.windows.camera:",
        "mail": "start outlookmail:",
        "photos": "start microsoft.photos:",

        # Communication
        "whatsapp": "start whatsapp:",
        "telegram": "telegram-desktop",
        "discord": "discord",
        "zoom": "zoom",

        # File/Cloud
        "onedrive": "onedrive",
    }

elif SYSTEM == "Linux":  # Ubuntu
    APPLICATIONS = {
        # System Tools
        "terminal": "gnome-terminal",
        "system monitor": "gnome-system-monitor",
        "settings": "gnome-control-center",

        # File Management
        "files": "nautilus",
        "file manager": "nautilus",

        # Browsers
        "firefox": "firefox",
        "chrome": "google-chrome",

        # Office
        "libreoffice writer": "libreoffice --writer",
        "libreoffice calc": "libreoffice --calc",
        "libreoffice impress": "libreoffice --impress",

        # Media
        "vlc": "vlc",
        "music": "rhythmbox",
        "videos": "totem",

        # Dev Tools
        "vscode": "code",
        "pycharm": "pycharm",
        "git": "git",

        # Utilities
        "calculator": "gnome-calculator",
        "text editor": "gedit",
        "screenshot": "gnome-screenshot",

        # Communication
        "telegram": "telegram-desktop",
        "discord": "discord",
        "zoom": "zoom",

        # Package manager
        "software center": "gnome-software",
    }

else:
    APPLICATIONS = {}