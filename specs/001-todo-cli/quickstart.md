# Quickstart Guide: Todo CLI Application

## Prerequisites

- Python 3.13 or higher
- uv package manager

## Setup

1. Clone the repository
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   uv venv
   uv pip install rich
   ```

## Running the Application

```bash
cd src
python -m todo.main
```

## Available Commands

- `add` - Add a new task
- `list` - View all tasks with status indicators
- `update <id>` - Update a task's title or description
- `delete <id>` - Delete a task by ID
- `complete <id>` - Mark a task as complete
- `incomplete <id>` - Mark a task as incomplete
- `help` - Show available commands
- `exit` or `quit` - Exit the application

## Example Usage

```
> add Buy groceries - Get milk, bread, and eggs
Task added successfully with ID: 1

> add Clean the house
Task added successfully with ID: 2

> list
┌─────┬─────────────────┬──────────────────────────┬──────────┐
│ ID  │ Title           │ Description              │ Status   │
├─────┼─────────────────┼──────────────────────────┼──────────┤
│ 1   │ Buy groceries   │ Get milk, bread, and eggs│ Pending  │
│ 2   │ Clean the house │                          │ Pending  │
└─────┴─────────────────┴──────────────────────────┴──────────┘

> complete 1
Task 1 marked as complete

> list
┌─────┬─────────────────┬──────────────────────────┬──────────┐
│ ID  │ Title           │ Description              │ Status   │
├─────┼─────────────────┼──────────────────────────┼──────────┤
│ 1   │ Buy groceries   │ Get milk, bread, and eggs│ Complete │
│ 2   │ Clean the house │                          │ Pending  │
└─────┴─────────────────┴──────────────────────────┴──────────┘
```