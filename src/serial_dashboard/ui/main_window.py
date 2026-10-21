"""
Module: main_window.py
Purpose:
    Application Main Window

Responsibilities:
    - Initialize Main Window
    - Set Window Layout

Dependecies:
    None
"""


from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Serial Dashboard")


