from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class ParticipantScreen(QWidget):
    def __init__(self, app_window):
        super().__init__()
        self.app_window = app_window

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Nama peserta")

        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("ID peserta")

        form = QFormLayout()
        form.addRow("Nama", self.name_input)
        form.addRow("ID", self.id_input)

        back_button = QPushButton("Kembali")
        back_button.clicked.connect(self.app_window.show_welcome_screen)

        next_button = QPushButton("Lanjut")
        next_button.clicked.connect(self.save_and_continue)

        actions = QHBoxLayout()
        actions.addWidget(back_button)
        actions.addStretch()
        actions.addWidget(next_button)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(form)
        layout.addLayout(actions)

    def reset_form(self):
        self.name_input.clear()
        self.id_input.clear()

    def save_and_continue(self):
        self.app_window.session_manager.set_participant(
            {
                "name": self.name_input.text().strip(),
                "participant_id": self.id_input.text().strip(),
            }
        )
        self.app_window.show_task_screen()
