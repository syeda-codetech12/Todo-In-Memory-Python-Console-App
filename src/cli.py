"""CLI interface for the Todo CLI application using Rich library."""

from typing import Optional
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

try:
    from .manager import TaskManager
except ImportError:
    # Fallback for direct execution
    from manager import TaskManager


class TodoCLI:
    """Handles user interaction using Rich for enhanced terminal output."""

    def __init__(self, task_manager: TaskManager) -> None:
        """Initialize the CLI with a TaskManager instance."""
        self.task_manager = task_manager
        self.console = Console()

    def display_tasks(self) -> None:
        """Display all tasks in a Rich table with status indicators."""
        tasks = self.task_manager.get_all_tasks()

        if not tasks:
            self.console.print("[yellow]No tasks found.[/yellow]")
            return

        table = Table(title="Todo List")
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Title", style="magenta")
        table.add_column("Description", style="green")
        table.add_column("Status", style="bold")

        for task in tasks:
            status = "[green]✓[/green]" if task.completed else "[red]○[/red]"
            description = task.description if task.description else ""
            table.add_row(str(task.id), task.title, description, status)

        self.console.print(table)

    def add_task(self) -> None:
        """Add a new task via CLI prompts."""
        try:
            title = Prompt.ask("[bold blue]Enter task title[/bold blue]")
            description_input = Prompt.ask(
                "[bold blue]Enter task description (optional, press Enter to skip)[/bold blue]", default=""
            )
            description = description_input if description_input.strip() else None

            task = self.task_manager.add_task(title, description)
            self.console.print(f"[green]Task added successfully with ID: {task.id}[/green]")
        except ValueError as e:
            self.console.print(f"[red]Error: {str(e)}[/red]")

    def update_task(self) -> None:
        """Update a task via CLI prompts."""
        try:
            task_id_str = Prompt.ask("[bold blue]Enter task ID to update[/bold blue]")
            task_id = int(task_id_str)

            task = self.task_manager.get_task_by_id(task_id)
            if task is None:
                self.console.print(f"[red]Error: Task with ID {task_id} not found[/red]")
                return

            title_input = Prompt.ask(
                f"[bold blue]Enter new title (current: {task.title}, press Enter to keep current)[/bold blue]",
                default=task.title
            )
            description_input = Prompt.ask(
                f"[bold blue]Enter new description (current: {task.description or ''}, press Enter to keep current)[/bold blue]",
                default=task.description or ""
            )

            title = title_input if title_input != task.title else None
            description = description_input if description_input != (task.description or "") else None

            if title is not None or description is not None:
                success = self.task_manager.update_task(task_id, title, description)
                if success:
                    self.console.print(f"[green]Task {task_id} updated successfully[/green]")
                else:
                    self.console.print(f"[red]Error: Failed to update task {task_id}[/red]")
            else:
                self.console.print("[yellow]No changes made to the task.[/yellow]")

        except ValueError:
            self.console.print("[red]Error: Please enter a valid task ID (number)[/red]")

    def delete_task(self) -> None:
        """Delete a task by ID via CLI prompt."""
        try:
            task_id_str = Prompt.ask("[bold blue]Enter task ID to delete[/bold blue]")
            task_id = int(task_id_str)

            success = self.task_manager.delete_task(task_id)
            if success:
                self.console.print(f"[green]Task {task_id} deleted successfully[/green]")
            else:
                self.console.print(f"[red]Error: Task with ID {task_id} not found[/red]")
        except ValueError:
            self.console.print("[red]Error: Please enter a valid task ID (number)[/red]")

    def mark_task_complete(self) -> None:
        """Mark a task as complete via CLI prompt."""
        try:
            task_id_str = Prompt.ask("[bold blue]Enter task ID to mark as complete[/bold blue]")
            task_id = int(task_id_str)

            success = self.task_manager.mark_task_complete(task_id)
            if success:
                self.console.print(f"[green]Task {task_id} marked as complete[/green]")
            else:
                self.console.print(f"[red]Error: Task with ID {task_id} not found[/red]")
        except ValueError:
            self.console.print("[red]Error: Please enter a valid task ID (number)[/red]")

    def mark_task_incomplete(self) -> None:
        """Mark a task as incomplete via CLI prompt."""
        try:
            task_id_str = Prompt.ask("[bold blue]Enter task ID to mark as incomplete[/bold blue]")
            task_id = int(task_id_str)

            success = self.task_manager.mark_task_incomplete(task_id)
            if success:
                self.console.print(f"[green]Task {task_id} marked as incomplete[/green]")
            else:
                self.console.print(f"[red]Error: Task with ID {task_id} not found[/red]")
        except ValueError:
            self.console.print("[red]Error: Please enter a valid task ID (number)[/red]")

    def show_help(self) -> None:
        """Display available commands with descriptions."""
        self.console.print("\n[bold]Available Commands:[/bold]")
        self.console.print("  add     - Add a new task")
        self.console.print("  list    - View all tasks with status indicators")
        self.console.print("  update  - Update a task's title or description")
        self.console.print("  delete  - Delete a task by ID")
        self.console.print("  complete - Mark a task as complete")
        self.console.print("  incomplete - Mark a task as incomplete")
        self.console.print("  help    - Show available commands")
        self.console.print("  exit    - Exit the application")

    def run(self) -> None:
        """
        Run the interactive command loop.

        This method provides the main application loop that continuously
        prompts the user for commands and executes the corresponding actions.
        """
        self.console.print("[bold green]Welcome to the Todo CLI Application![/bold green]")
        self.console.print("Type 'help' for available commands or 'exit' to quit.\n")

        while True:
            try:
                command = Prompt.ask("\n[bold yellow]Enter command[/bold yellow]").strip().lower()

                if command in ["exit", "quit"]:
                    self.console.print("[bold green]Goodbye![/bold green]")
                    break
                elif command == "add":
                    self.add_task()
                elif command == "list":
                    self.display_tasks()
                elif command == "update":
                    self.update_task()
                elif command == "delete":
                    self.delete_task()
                elif command == "complete":
                    self.mark_task_complete()
                elif command == "incomplete":
                    self.mark_task_incomplete()
                elif command == "help":
                    self.show_help()
                else:
                    self.console.print(f"[red]Unknown command: {command}. Type 'help' for available commands.[/red]")

            except KeyboardInterrupt:
                self.console.print("\n[bold green]Goodbye![/bold green]")
                break
            except EOFError:
                self.console.print("\n[bold green]Goodbye![/bold green]")
                break