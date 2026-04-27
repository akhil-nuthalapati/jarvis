import subprocess
import os
import platform
from config import APPLICATIONS


class AppLauncher:
    def __init__(self):
        self.apps = APPLICATIONS
        self.system = platform.system()

    def launch(self, app_name):
        app_name = app_name.lower().strip()

        # Find app (exact or partial)
        for name, path in self.apps.items():
            if app_name == name or app_name in name:
                return self._run(path)

        print(f"App not found: {app_name}")
        return False

    def _run(self, command):
        try:
            if self.system == "Windows":
                if command.startswith("ms-") or command.startswith("start"):
                    os.startfile(command)
                else:
                    subprocess.Popen(command, shell=True)

            else:  # Linux (Ubuntu)
                subprocess.Popen(
                    command.split(),
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )

            print(f"Launched: {command}")
            return True

        except Exception as e:
            print(f"Launch error: {e}")
            return False