"""
Module:app.py
Purpose:
    Application Entry Point

Responsibilities:
    - Load and validate application Entry Point
    - Initialize shared application state
    - Start the main application loop
    - Handle resouce cleanup

Dependecies:
    - main_window: main window configs
"""

import sys

from PySide6.QtWidgets import QApplication

from serial_dashboard.ui.main_window import MainWindow


# --- Main Application Entry ---
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Serial Dashboard")
    window = MainWindow()
    window.show()
    return app.exec() # Main app loop


if __name__ == "__main__":
    raise SystemExit(main())
