from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget


class TaskScreen(QWidget):
    def __init__(self, app_window):
        super().__init__()
        self.app_window = app_window

        label = QLabel("Halaman tugas")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 22px; font-weight: 600;")

        finish_button = QPushButton("Selesai")
        finish_button.clicked.connect(self.finish_task)

        layout = QVBoxLayout(self)
        layout.addStretch()
        layout.addWidget(label)
        layout.addWidget(finish_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()

    def finish_task(self):
        self.app_window.session_manager.set_task_result({"status": "completed"})
        self.app_window.show_result_screen()
