# Copyright (c) 2024-2026 Daniel Seichter
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

import gui_about
import webbrowser


class DialogAbout(gui_about.DialogAbout):
    def __init__(self, parent=None):
        super().__init__(parent)
    
    def openGithub(self, event):
        """Open GitHub repository"""
        webbrowser.open_new_tab("https://github.com/dseichter/VATValidation")