"""Task data model for the Todo CLI application."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo item with id, title, description, and completion status.

    Attributes:
        id (int): Unique incremental identifier for the task
        title (str): Required title of the task
        description (Optional[str]): Optional detailed description of the task
        completed (bool): Status indicator showing if the task is completed (default: False)
    """

    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

    def __post_init__(self) -> None:
        """Validate Task fields after initialization."""
        if self.id <= 0:
            raise ValueError("Task ID must be a positive integer")
        if not self.title.strip():
            raise ValueError("Task title cannot be empty")
        if not isinstance(self.completed, bool):
            raise ValueError("Task completed status must be a boolean")