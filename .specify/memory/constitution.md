<!--
Sync Impact Report:
- Version change: N/A → 1.0.0
- Modified principles: N/A (new constitution)
- Added sections: All sections added
- Removed sections: N/A
- Templates requiring updates:
  - .specify/templates/plan-template.md ✅ updated
  - .specify/templates/spec-template.md ✅ updated
  - .specify/templates/tasks-template.md ✅ updated
  - .specify/templates/commands/*.md ✅ reviewed
- Follow-up TODOs: None
-->
# Python Console Todo Application Constitution

## Core Principles

### Technology Stack Constraint
All code must be written in Python 3.13+ with no external dependencies beyond the Python standard library. This ensures maximum portability and eliminates dependency management complexity. In-memory storage only - no database or file persistence is allowed, maintaining simplicity and avoiding filesystem dependencies.

### Project Structure
The project follows a clean, modular Python layout with a /src folder containing the main package/code. The main entry point is src/main.py with a simple CLI loop. Separate modules must exist for task model, storage, and CLI commands to maintain clear separation of concerns and improve maintainability.

### Code Quality and Style
All code must follow PEP 8 style guidelines with type hints used everywhere. Code must be clear, readable, well-documented with docstrings, and prefer simple, explicit implementations over clever shortcuts. Defensive programming practices are required: all inputs must be validated and errors handled gracefully to ensure robust operation.

### Architectural Separation
The system maintains strict separation of concerns between model, storage, and UI/CLI layers. Tasks are stored in a simple in-memory list or manager class with unique incremental integer IDs assigned to each task. The task model must include id (int), title (str), description (str, optional), and completed (bool) fields to maintain consistency.

### Task Management Model
The application manages tasks using a simple in-memory list structure with unique incremental integer IDs. Each task must have id (int), title (str), description (str, optional), and completed (bool) properties. This provides a consistent, predictable interface for task management operations while maintaining simplicity.

### Development Process Discipline
No code implementation is permitted until specifications, plan, and tasks are complete and validated. All implementation must trace back to explicit tasks to maintain project discipline. The focus must be on simplicity, reliability, and creating a user-friendly console experience that meets user expectations.

## Console Application Behavior

The application provides an interactive command-line menu or command-based interface with clear prompts and feedback. Status indicators must be used when listing tasks (e.g., [x] for completed, [ ] for pending) to provide visual clarity. The application must gracefully handle invalid inputs with appropriate error messages and recovery.

## Development Workflow

The project uses uv for virtual environment and scripting management to ensure consistent development environments. The workflow requires completing specifications, plans, and tasks before any implementation begins. All changes must be traceable back to specific tasks, and the focus remains on delivering simple, reliable functionality with a user-friendly console experience.

## Governance

This constitution supersedes all other development practices and standards for this project. All code changes must comply with these principles before being accepted. Amendments to this constitution require explicit documentation, approval from project maintainers, and a migration plan for existing code. All pull requests and reviews must verify compliance with these principles. The constitution serves as the authoritative source for development decisions and quality standards.

**Version**: 1.0.0 | **Ratified**: 2025-12-31 | **Last Amended**: 2025-12-31