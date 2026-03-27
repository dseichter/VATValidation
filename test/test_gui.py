import pytest
from PySide6.QtWidgets import QMessageBox, QApplication
from PySide6.QtCore import Qt
from PIL import ImageGrab
import sys
import os
import json


sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from vatvalidation import VATValidationFrame


def take_screenshot(app, filename):
    """Take screenshot of widget content"""

    screenshot = app.grab()
    screenshot.save(filename)
    print(f"Widget screenshot saved to {filename}")


def take_full_screenshot(app, filename):
    """Take screenshot of active window only using PIL"""
    # Get window geometry
    geometry = app.frameGeometry()
    
    screenshot = ImageGrab.grab(bbox=(
        geometry.x(),
        geometry.y(),
        geometry.x() + geometry.width(),
        geometry.y() + geometry.height()
    ))
    screenshot.save(filename)
    print(f"App screenshot saved to {filename}")


@pytest.fixture
def app(qtbot, tmp_path, monkeypatch):
    """Create application instance"""
    # Create temporary config file
    config_file = tmp_path / "config.json"
    config_data = {
        "ownvat": "DE123456789",
        "interface": "bzst",
        "language": "en",
        "delimiter": ";",
        "logfilename": "",
        "loglevel": "ERROR",
        "proxy_mode": "none",
        "proxy_password": "",
        "proxy_url": "",
        "proxy_username": "",
        "theme": "light"
    }
    config_file.write_text(json.dumps(config_data))

    # create screenshots folder, if not exists
    if not os.path.exists("test/screenshots"):
        os.makedirs("test/screenshots")
    
    # Mock settings to use temp config
    monkeypatch.setattr("settings.CONFIGFILE", str(config_file))
    
    test_app = VATValidationFrame()
    qtbot.addWidget(test_app)
    yield test_app
    test_app.close()


def test_single_tab(app, qtbot, monkeypatch):
    """Test single validation tab"""
    app.show()
    qtbot.waitExposed(app)
    
    # Switch to single tab
    app.tab_widget.setCurrentIndex(0)
    
    # Fill in values
    app.textOwnvat.setText("DE123456789")
    app.textForeignvat.setText("ATU123456789")
    qtbot.wait(200)

    monkeypatch.setattr(QMessageBox, "information", lambda *args, **kwargs: QMessageBox.Ok)
    monkeypatch.setattr(
        "single.validatesingle",
        lambda **kwargs: {
            "key1": "",
            "key2": "",
            "ownvat": kwargs.get("ownvat", ""),
            "foreignvat": kwargs.get("foreignvat", ""),
            "type": "vies",
            "valid": True,
            "errorcode": "VALID",
            "errorcode_description": "VAT number is valid",
            "valid_from": "",
            "valid_to": "",
            "timestamp": "2026-03-27T00:00:00",
            "company": "",
            "address": "",
            "town": "",
            "zip": "",
            "street": "",
        },
    )
    qtbot.mouseClick(app.buttonValidateSingle, Qt.LeftButton, delay=1)
    qtbot.waitUntil(lambda: app.textResultIsValid.text() in ("Yes", "No"), timeout=3000)
    qtbot.waitUntil(lambda: app.textResultCode.text() == "VALID", timeout=3000)
    qtbot.waitUntil(
        lambda: "Interface:" in app.m_staticText_ValidationResult.text(),
        timeout=3000,
    )
    qtbot.waitUntil(lambda: app.textResultDetails.toPlainText() != "", timeout=3000)
    # Flush queued paint events so screenshots reflect the final rendered state.
    QApplication.processEvents()
    qtbot.wait(200)
    
    take_screenshot(app, "test/screenshots/single_tab.png")
    take_full_screenshot(app, "docs/docs/assets/single.png")
    
    assert app.tab_widget.currentIndex() == 0


def test_batch_tab(app, qtbot):
    """Test batch processing tab"""
    app.show()
    qtbot.waitExposed(app)
    
    # Switch to batch tab
    app.tab_widget.setCurrentIndex(1)
    
    # Fill in file paths
    app.textInputFile.setText("/home/dseichter/testdata/vat/ustid-30.csv")
    app.textOutputFile.setText("/home/dseichter/testdata/vat/ustid-30-log.csv")
    qtbot.wait(200)
    
    take_screenshot(app, "test/screenshots/batch_tab.png")
    take_full_screenshot(app, "docs/docs/assets/batch.png")
    
    assert app.tab_widget.currentIndex() == 1


def test_config_tab(app, qtbot):
    """Test configuration tab"""
    app.show()
    qtbot.waitExposed(app)
    
    # Switch to config tab
    app.tab_widget.setCurrentIndex(2)
    
    # Fill in config values
    app.textCtrlConfigOwnVat.setText("DE123456789")
    app.comboBoxConfigInterface.setCurrentText("vies")
    app.comboBoxConfigLanguage.setCurrentText("en")
    app.textConfigCSVdelimiter.setText(";")
    app.comboBoxConfigProxyMode.setCurrentText("manual")
    app.textConfigProxyUrl.setText("http://proxy.example.com:8080") # NOSONAR
    app.textConfigProxyUsername.setText("user")
    app.textConfigProxyPassword.setText("secret")
    qtbot.wait(200)
    
    take_screenshot(app, "test/screenshots/config_tab.png")
    take_full_screenshot(app, "docs/docs/assets/config.png")
    
    assert app.tab_widget.currentIndex() == 2
