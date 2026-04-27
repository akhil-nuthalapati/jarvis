"""
Application Launcher Module
Author: Person 5
Purpose: Launches system applications
"""

import subprocess
import os
import platform
from config import APPLICATIONS


class AppLauncher:
    """
    Handles launching applications on the system.
    """
    
    def __init__(self):
        self.apps = APPLICATIONS
        self.system = platform.system()
    
    def launch(self, app_name):
        """
        Launches an application by name.
        
        Args:
            app_name: Name of the application to launch
            
        Returns:
            bool: True if launch successful, False otherwise
        """
        app_name = app_name.lower().strip()
        
        # Find matching application
        app_path = self._find_app(app_name)
        
        if app_path:
            return self._execute(app_path)
        
        return False
    
    def _find_app(self, app_name):
        """
        Finds the application path from configured apps.
        Supports partial matching.
        """
        # Exact match
        if app_name in self.apps:
            return self.apps[app_name]
        
        # Partial match
        for name, path in self.apps.items():
            if app_name in name or name in app_name:
                return path
        
        return None
    
    def _execute(self, app_path):
        """
        Executes the application.
        
        Args:
            app_path: Path to the application
            
        Returns:
            bool: True if successful
        """
        try:
            if self.system == "Windows":
                # Handle Windows-specific launches
                if app_path.startswith("ms-"):
                    # Windows Settings URI
                    os.startfile(app_path)
                else:
                    subprocess.Popen(app_path, shell=True)
                    
            elif self.system == "Darwin":
                # macOS
                subprocess.Popen(["open", app_path])
                
            else:
                # Linux
                subprocess.Popen([app_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            print(f"Launched: {app_path}")
            return True
            
        except FileNotFoundError:
            print(f"Application not found: {app_path}")
            return False
            
        except Exception as e:
            print(f"Error launching application: {e}")
            return False
    
    def list_available_apps(self):
        """
        Returns list of available application names.
        """
        return list(self.apps.keys())
    
    def add_app(self, name, path):
        """
        Adds a new application to the launcher.
        
        Args:
            name: Application name (for voice command)
            path: System path to the application
        """
        self.apps[name.lower()] = path
