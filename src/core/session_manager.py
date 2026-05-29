from dataclasses import dataclass, field
from typing import Any


@dataclass
class SessionManager:
    participant: dict[str, Any] = field(default_factory=dict)
    task_result: dict[str, Any] = field(default_factory=dict)

    def set_participant(self, data: dict[str, Any]):
        self.participant = data

    def set_task_result(self, data: dict[str, Any]):
        self.task_result = data

    def reset(self):
        self.participant.clear()
        self.task_result.clear()
