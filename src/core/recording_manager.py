class ScreenRecordingManager:
    def __init__(self):
        self.is_recording = False

    def start_recording(self):
        self.is_recording = True

    def stop_recording(self):
        self.is_recording = False
