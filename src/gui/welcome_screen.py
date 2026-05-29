from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget


class WelcomeScreen(QWidget):
    def __init__(self, app_window):
        super().__init__()
        self.app_window = app_window

        title = QLabel("QuickScore UI")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 28px; font-weight: 700;")

        start_button = QPushButton("Mulai")
        start_button.clicked.connect(self.app_window.show_participant_screen)

        layout = QVBoxLayout(self)
        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(start_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()
