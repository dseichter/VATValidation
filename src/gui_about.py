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

from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QDialogButtonBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap

import helper
import icons


class DialogAbout(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About VATValidation")
        self.setFixedSize(240, 200)
        self.setWindowIcon(icons.get_icon('select_check_box_48dp_097e23_fill1_wght400_grad0_opsz48'))
        
        layout = QVBoxLayout(self)
        
        # Logo
        logo_label = QLabel()
        icon = icons.get_icon('select_check_box_24dp_097e23_fill1_wght400_grad0_opsz24')
        pixmap = icon.pixmap(24, 24)
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label)
        
        # Name and version
        name_label = QLabel(f"{helper.NAME} {helper.VERSION}")
        name_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(name_label)
        
        # License
        license_label = QLabel(f"Licensed under {helper.LICENCE}")
        license_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(license_label)
        
        # GitHub link
        self.github_label = QLabel("More on GitHub")
        font = self.github_label.font()
        font.setUnderline(True)
        self.github_label.setFont(font)
        self.github_label.setStyleSheet("color: blue;")
        self.github_label.setAlignment(Qt.AlignCenter)
        self.github_label.setToolTip("Visit GitHub repository for further information.")
        self.github_label.mousePressEvent = self.openGithub
        layout.addWidget(self.github_label)
        
        # Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
        # Center the dialog
        self.move_to_center()
    
    def move_to_center(self):
        """Center the dialog on the screen"""
        if self.parent():
            parent_rect = self.parent().geometry()
            x = parent_rect.x() + (parent_rect.width() - self.width()) // 2
            y = parent_rect.y() + (parent_rect.height() - self.height()) // 2
            self.move(max(x, 0), max(y, 0))
    
    def openGithub(self, event):
        """Virtual event handler - to be implemented in subclass"""
        pass