"""TaskManager for the Todo CLI application."""

from typing import List, Optional

try:
    from .models import Task
except ImportError:
    # Fallback for direct execution
    from models import Task


class TaskManager:
    """
    Manages in-memory collection of Task entities with operations to manage them.

    This class handles all storage and business logic operations for tasks:
    add, update, delete, mark complete, etc. It stores tasks in memory only.
    """

    def __init__(self) -> None:
        """Initialize the TaskManager with an empty list of tasks and next ID counter."""
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Create a new task with auto-generated ID.

        Args:
            title (str): The title of the task (required)
            description (Optional[str]): The description of the task (optional)

        Returns:
            Task: The newly created Task object with auto-generated unique ID

        Raises:
            ValueError: If title is empty or None
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")

        task = Task(id=self._next_id, title=title.strip(), description=description, completed=False)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Return all tasks in the collection.

        Returns:
            List[Task]: A list of all Task objects in the manager
        """
        return self._tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Return a specific task by ID.

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Optional[Task]: The Task object if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update task details.

        Args:
            task_id (int): The ID of the task to update
            title (Optional[str]): New title for the task (optional)
            description (Optional[str]): New description for the task (optional)

        Returns:
            bool: True if the task was found and updated, False otherwise

        Raises:
            ValueError: If title is provided but is empty
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        if title is not None:
            if not title.strip():
                raise ValueError("Title cannot be empty")
            task.title = title.strip()

        if description is not None:
            task.description = description

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task from the collection.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if the task was found and removed, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        self._tasks.remove(task)
        return True

    def mark_task_complete(self, task_id: int) -> bool:
        """
        Set task completion status to True.

        Args:
            task_id (int): The ID of the task to mark as complete

        Returns:
            bool: True if the task was found and updated, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.completed = True
        return True

    def mark_task_incomplete(self, task_id: int) -> bool:
        """
        Set task completion status to False.

        Args:
            task_id (int): The ID of the task to mark as incomplete

        Returns:
            bool: True if the task was found and updated, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.completed = False
        return True