"""Main entry point for the Todo CLI application."""

import sys
import os

# Add the src directory to the path for direct execution
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from .manager import TaskManager
    from .cli import TodoCLI
except ImportError:
    # Fallback for direct execution
    from manager import TaskManager
    from cli import TodoCLI


def main() -> None:
    """
    Main entry point that initializes TaskManager and starts CLI.

    This function creates a TaskManager instance, initializes the CLI with it,
    and runs the interactive command loop.
    """
    task_manager = TaskManager()
    cli = TodoCLI(task_manager)
    cli.run()


if __name__ == "__main__":
    main()