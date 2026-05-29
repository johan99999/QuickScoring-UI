import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget

try:
    from .core.camera_manager import CameraManager
    from .core.recording_manager import ScreenRecordingManager
    from .core.session_manager import SessionManager
    from .gui.participant_screen import ParticipantScreen
    from .gui.result_screen import ResultScreen
    from .gui.task_screen import TaskScreen
    from .gui.welcome_screen import WelcomeScreen
    from .utils.file_utils import StateManager
except ImportError:
    from core.camera_manager import CameraManager
    from core.recording_manager import ScreenRecordingManager
    from core.session_manager import SessionManager
    from gui.participant_screen import ParticipantScreen
    from gui.result_screen import ResultScreen
    from gui.task_screen import TaskScreen
    from gui.welcome_screen import WelcomeScreen
    from utils.file_utils import StateManager


class QuickScoreUIApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuickScore UI")
        self.resize(1000, 600)
        self.setStyleSheet("background-color: white;")

        self.session_manager = SessionManager()
        self.camera_manager = CameraManager()
        self.recording_manager = ScreenRecordingManager()
        self.state_manager = StateManager()

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.welcome_screen = WelcomeScreen(self)
        self.participant_screen = ParticipantScreen(self)
        self.task_screen = TaskScreen(self)
        self.result_screen = ResultScreen(self)

        self.stacked_widget.addWidget(self.welcome_screen)
        self.stacked_widget.addWidget(self.participant_screen)
        self.stacked_widget.addWidget(self.task_screen)
        self.stacked_widget.addWidget(self.result_screen)

        self.show_welcome_screen()

    def show_welcome_screen(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_participant_screen(self):
        self.participant_screen.reset_form()
        self.stacked_widget.setCurrentIndex(1)

    def show_task_screen(self):
        self.stacked_widget.setCurrentIndex(2)

    def show_result_screen(self):
        self.result_screen.refresh_session_data()
        self.stacked_widget.setCurrentIndex(3)

    def closeEvent(self, event):
        self.camera_manager.stop_camera()
        self.recording_manager.stop_recording()
        event.accept()


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("QuickScore UI")
    app.setApplicationVersion("0.1.0")
    app.setOrganizationName("QuickScore")
    app.setStyleSheet(
        """
        QWidget {
            background-color: white;
            color: black;
        }
        QMainWindow {
            background-color: white;
        }
        """
    )

    window = QuickScoreUIApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
