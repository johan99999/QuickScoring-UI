import json
from pathlib import Path
from typing import Any


class StateManager:
    def __init__(self, state_path: str | Path = "storage/storage.json"):
        self.state_path = Path(state_path)

    def load(self) -> dict[str, Any]:
        if not self.state_path.exists() or self.state_path.stat().st_size == 0:
            return {}
        with self.state_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def save(self, data: dict[str, Any]):
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        with self.state_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
