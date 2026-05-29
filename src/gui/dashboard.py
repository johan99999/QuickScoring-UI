from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget


class DashboardScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        label = QLabel("Dashboard")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 22px; font-weight: 600;")

        layout = QVBoxLayout(self)
        layout.addWidget(label)
