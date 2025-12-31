# Implementation Plan: Todo CLI Application

**Branch**: `001-todo-cli` | **Date**: 2025-12-31 | **Spec**: [link to spec](spec.md)
**Input**: Feature specification from `/specs/001-todo-cli/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a simple in-memory Python console Todo application with five core features: Add Task, View/List Tasks, Update Task, Delete Task by ID, and Mark Task as Complete/Incomplete. The application will follow separation of concerns with a Task model, TaskManager for storage and operations, and CLI module for user interaction. The implementation will use Python 3.13+ with Rich library for enhanced terminal output.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Rich library for terminal formatting, uv for package management
**Storage**: In-memory storage only (no persistent storage)
**Testing**: pytest for unit and integration testing
**Target Platform**: Cross-platform CLI application (Linux, macOS, Windows)
**Project Type**: Console application
**Performance Goals**: Sub-second response time for all operations, minimal memory footprint
**Constraints**: No external dependencies beyond Python standard library and Rich, in-memory only storage, terminal-based interface
**Scale/Scope**: Single-user application, up to hundreds of tasks in memory

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ✅ Technology Stack Constraint: Using Python 3.13+ with Rich library (minimal external dependency)
- ✅ Project Structure: Following clean, modular layout with /src folder
- ✅ Code Quality and Style: Will use type hints everywhere, follow PEP 8, include docstrings
- ✅ Architectural Separation: Clear separation between model, storage, and UI/CLI layers
- ✅ Task Management Model: Will use unique incremental integer IDs with required fields
- ✅ Development Process Discipline: Following spec → plan → tasks → implementation workflow
- ⚠️ Constitution Update Needed: Rich library dependency requires update to constitution to allow this external dependency beyond standard library

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-cli/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/todo/
├── __init__.py
├── models.py            # Task dataclass definition
├── manager.py           # TaskManager class for storage and operations
├── cli.py               # CLI interface using Rich library
└── main.py              # Entry point with interactive loop
```

**Structure Decision**: Single console application project following the clean, modular Python layout required by the constitution. The structure separates concerns with distinct modules for data model (models.py), business logic/storage (manager.py), user interface (cli.py), and application entry point (main.py).

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Rich library dependency | Enhanced terminal output with colored text, tables, and styled prompts improves user experience significantly | Plain text output would be less user-friendly and harder to read |

## Phase 0: Research

### Research Tasks

1. **Rich Library Integration**: Research best practices for using Rich library for CLI applications, including tables, prompts, and styled output
2. **Python 3.13+ Features**: Investigate any specific features of Python 3.13+ that could benefit the implementation
3. **Dataclass Patterns**: Research optimal patterns for dataclass usage in Python for the Task model
4. **CLI Architecture**: Research best practices for interactive CLI applications in Python

## Phase 1: Design & Architecture

### Architecture Overview

The application will follow a clean architecture pattern with three main components:

1. **Task Model** (`models.py`): A dataclass representing a single task with id, title, description, and completed status
2. **TaskManager** (`manager.py`): Handles all storage and business logic operations (add, update, delete, mark complete)
3. **CLI Interface** (`cli.py`): Handles user interaction using Rich for enhanced terminal output
4. **Main Entry Point** (`main.py`): Orchestrates the application flow

### Component Details

#### Task Model
- Dataclass with fields: id (int), title (str), description (str, optional), completed (bool)
- Default value for completed: False
- Validation for required fields

#### TaskManager
- In-memory storage using a list
- Auto-incrementing ID assignment
- Methods for all required operations: add, get_all, update, delete, mark_complete
- Input validation and error handling

#### CLI Interface
- Interactive loop with menu options
- Rich components for enhanced display:
  - Tables for listing tasks with status indicators
  - Styled prompts for user input
  - Colored feedback messages
  - Error handling with user-friendly messages

#### Main Entry Point
- Initialize TaskManager
- Start CLI interface
- Handle graceful shutdown

## Dependencies

- **Rich**: For enhanced terminal output (tables, colors, prompts)
- **Python Standard Library**: For all other functionality (dataclasses, typing, etc.)

## Implementation Approach

1. Set up project structure with uv and install Rich dependency
2. Implement Task model with dataclass
3. Create TaskManager with in-memory storage and all required operations
4. Build CLI interface with Rich components
5. Create main entry point and connect all components
6. Add comprehensive error handling and input validation
7. Test all functionality and refine user experience

## Feature Breakdown

### Add Task Feature
- Command: `add`
- Input: title (required), description (optional)
- Output: Success message with task ID
- Validation: Title cannot be empty

### View/List Tasks Feature
- Command: `list`
- Output: Table with ID, title, description, and status indicator
- Status indicators: [green]✓[/] for completed, [red]○[/] for pending

### Update Task Feature
- Command: `update <id>`
- Input: task ID, new title/description
- Output: Success confirmation
- Validation: Task exists, valid ID format

### Delete Task Feature
- Command: `delete <id>`
- Input: task ID
- Output: Success confirmation
- Validation: Task exists, valid ID format

### Mark Task Complete/Incomplete Feature
- Commands: `complete <id>`, `incomplete <id>`
- Input: task ID
- Output: Status change confirmation
- Validation: Task exists, valid ID format
