from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget


class ResultScreen(QWidget):
    def __init__(self, app_window):
        super().__init__()
        self.app_window = app_window

        self.summary = QLabel()
        self.summary.setAlignment(Qt.AlignmentFlag.AlignCenter)

        restart_button = QPushButton("Ulangi")
        restart_button.clicked.connect(self.restart)

        layout = QVBoxLayout(self)
        layout.addStretch()
        layout.addWidget(self.summary)
        layout.addWidget(restart_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()

    def refresh_session_data(self):
        participant = self.app_window.session_manager.participant
        name = participant.get("name") or "Peserta"
        status = self.app_window.session_manager.task_result.get("status", "belum selesai")
        self.summary.setText(f"{name}: {status}")

    def restart(self):
        self.app_window.session_manager.reset()
        self.app_window.show_welcome_screen()
