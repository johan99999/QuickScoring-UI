from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout


class StatusDialog(QDialog):
    def __init__(self, message="Status", parent=None):
        super().__init__(parent)
        self.setWindowTitle("Status")

        self.message_label = QLabel(message)

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)

        layout = QVBoxLayout(self)
        layout.addWidget(self.message_label)
        layout.addWidget(ok_button)
