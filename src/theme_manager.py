# Copyright (c) 2024-2025 Daniel Seichter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSettings
from PySide6.QtGui import QPalette, QColor


class ThemeManager:
    @staticmethod
    def apply_theme(theme_name):
        """Apply theme to the application"""
        app = QApplication.instance()
        if not app:
            return
            
        if theme_name == "dark":
            ThemeManager._apply_dark_theme(app)
        elif theme_name == "light":
            ThemeManager._apply_light_theme(app)
        else:  # system
            ThemeManager._apply_system_theme(app)
    
    @staticmethod
    def _apply_dark_theme(app):
        """Apply dark theme"""
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(43, 43, 43))
        dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Base, QColor(30, 30, 30))
        dark_palette.setColor(QPalette.AlternateBase, QColor(60, 60, 60))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(0, 0, 0))
        dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        dark_palette.setColor(QPalette.Link, QColor(66, 165, 245))
        dark_palette.setColor(QPalette.Highlight, QColor(66, 165, 245))
        dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))
        app.setPalette(dark_palette)
    
    @staticmethod
    def _apply_light_theme(app):
        """Apply light theme"""
        light_palette = QPalette()
        light_palette.setColor(QPalette.Window, QColor(240, 240, 240))
        light_palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
        light_palette.setColor(QPalette.Base, QColor(255, 255, 255))
        light_palette.setColor(QPalette.AlternateBase, QColor(245, 245, 245))
        light_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 220))
        light_palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))
        light_palette.setColor(QPalette.Text, QColor(0, 0, 0))
        light_palette.setColor(QPalette.Button, QColor(240, 240, 240))
        light_palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
        light_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
        light_palette.setColor(QPalette.Link, QColor(0, 0, 255))
        light_palette.setColor(QPalette.Highlight, QColor(0, 120, 215))
        light_palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
        app.setPalette(light_palette)
    
    @staticmethod
    def _apply_system_theme(app):
        """Apply system theme"""
        import os
        # Check for dark mode on different platforms
        is_dark = False
        
        # macOS
        if os.name == 'posix' and 'darwin' in os.uname().sysname.lower():
            try:
                import subprocess
                result = subprocess.run(['defaults', 'read', '-g', 'AppleInterfaceStyle'], 
                                      capture_output=True, text=True)
                is_dark = result.stdout.strip() == 'Dark'
            except:
                pass
        
        # Linux (check for dark theme)
        elif os.name == 'posix':
            try:
                import subprocess
                result = subprocess.run(['gsettings', 'get', 'org.gnome.desktop.interface', 'gtk-theme'], 
                                      capture_output=True, text=True)
                is_dark = 'dark' in result.stdout.lower()
            except:
                pass
        
        if is_dark:
            ThemeManager._apply_dark_theme(app)
        else:
            ThemeManager._apply_light_theme(app)