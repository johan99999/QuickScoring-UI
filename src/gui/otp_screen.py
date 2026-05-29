from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class OtpScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        title = QLabel("OTP")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 22px; font-weight: 600;")

        self.otp_input = QLineEdit()
        self.otp_input.setPlaceholderText("Kode OTP")

        self.verify_button = QPushButton("Verifikasi")

        layout = QVBoxLayout(self)
        layout.addWidget(title)
        layout.addWidget(self.otp_input)
        layout.addWidget(self.verify_button)
