import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

# Import screens
from gui.welcome_screen import WelcomeScreen
from gui.participant_screen import ParticipantScreen  
from gui.task_screen import TaskScreen
from gui.result_screen import ResultScreen

# Import core managers
from core.session_manager import SessionManager
from core.camera_manager import CameraManager
from core.recording_manager import ScreenRecordingManager
from utils.file_utils import StateManager


class QuickScoreUIApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuickScore UI")
        
        screen = QApplication.primaryScreen().geometry()
        self.resize(1000, 300)
        self.setStyleSheet("background-color: white;")
        
        # Initialize managers
        self.session_manager = SessionManager()
        self.camera_manager = CameraManager()
        self.recording_manager = ScreenRecordingManager()
        self.state_manager = StateManager()
        
        # Create central widget with stacked layout
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # Initialize screens
        self.welcome_screen = WelcomeScreen(self)
        self.participant_screen = ParticipantScreen(self)
        self.task_screen = TaskScreen(self)
        self.result_screen = ResultScreen(self)
        
        # Add screens to stack
        self.stacked_widget.addWidget(self.welcome_screen)      # Index 0
        self.stacked_widget.addWidget(self.participant_screen)  # Index 1
        self.stacked_widget.addWidget(self.task_screen)         # Index 2
        self.stacked_widget.addWidget(self.result_screen)       # Index 3
        
        # Start with welcome screen
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
        # Clean up resources
        self.camera_manager.stop_camera()
        self.recording_manager.stop_recording()
        event.accept()


def main():
    app = QApplication(sys.argv)
    
    app.setApplicationName("QuickScore UI")
    app.setApplicationVersion("0.1.0")
    app.setOrganizationName("QuickScore")
    
    app.setStyleSheet("""
        QWidget {
            background-color: white;
            color: black;
        }
        QMainWindow {
            background-color: white;
        }
    """)
    
    window = QuickScoreUIApp()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
