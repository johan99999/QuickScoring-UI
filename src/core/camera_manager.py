class CameraManager:
    def __init__(self):
        self.is_running = False

    def start_camera(self):
        self.is_running = True

    def stop_camera(self):
        self.is_running = False
