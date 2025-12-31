# Implementation Tasks: Todo CLI Application

**Feature**: Todo CLI Application
**Branch**: 001-todo-cli
**Created**: 2025-12-31
**Input**: Feature specification from `/specs/001-todo-cli/spec.md`, Plan from `/specs/001-todo-cli/plan.md`

## Dependencies

- **User Story 1 (P1)**: [US1] Add New Tasks - Foundation for all other features
- **User Story 2 (P1)**: [US2] View/List All Tasks - Requires US1 for data
- **User Story 3 (P2)**: [US3] Mark Tasks as Complete/Incomplete - Requires US1 for data
- **User Story 4 (P2)**: [US4] Update Task Details - Requires US1 for data
- **User Story 5 (P3)**: [US5] Delete Tasks by ID - Requires US1 for data

## Implementation Strategy

**MVP Scope**: Implement US1 (Add Tasks) and US2 (View/List Tasks) as minimum viable product, then add remaining features incrementally.

**Parallel Execution Opportunities**:
- US3, US4, and US5 can be implemented in parallel after US1 is complete
- Model and CLI components can be developed in parallel once the interface is defined

---

## Phase 1: Setup

- [ ] T001 Create project structure with src/todo/ directory per plan.md
- [ ] T002 Create __init__.py in src/todo/ directory per plan.md
- [ ] T003 Install Rich library dependency via `uv add rich` per plan.md
- [ ] T004 [P] Create models.py file in src/todo/ per plan.md
- [ ] T005 [P] Create manager.py file in src/todo/ per plan.md
- [ ] T006 [P] Create cli.py file in src/todo/ per plan.md
- [ ] T007 [P] Create main.py file in src/todo/ per plan.md

## Phase 2: Foundational Components

- [ ] T008 Implement Task dataclass in src/todo/models.py with id, title, description, completed fields per plan.md and data-model.md
- [ ] T009 Add type hints and validation to Task dataclass per constitution.md
- [ ] T010 Implement TaskManager class in src/todo/manager.py with in-memory storage per plan.md and data-model.md
- [ ] T011 Implement add_task method in TaskManager with auto-incrementing ID per data-model.md
- [ ] T012 Implement get_all_tasks method in TaskManager per data-model.md
- [ ] T013 Implement get_task_by_id method in TaskManager per data-model.md

## Phase 3: User Story 1 - Add New Tasks (P1)

**Goal**: Enable users to add new tasks to their todo list with a title and optional description per spec.md

**Independent Test**: Can be fully tested by adding tasks through the CLI interface and verifying they appear in the list, delivering the core value of task management per spec.md

**Tests**:
- [ ] T014 [P] [US1] Test that add_task creates task with unique ID and title
- [ ] T015 [P] [US1] Test that add_task accepts optional description
- [ ] T016 [P] [US1] Test that add_task validates non-empty title

**Implementation**:
- [ ] T017 [US1] Implement add_task method in TaskManager with title validation per data-model.md
- [ ] T018 [US1] Implement add command in CLI interface using Rich Prompt per plan.md
- [ ] T019 [US1] Implement CLI add command that calls TaskManager.add_task per spec.md
- [ ] T020 [US1] Implement CLI add command output with task ID per spec.md and contracts/cli-api.md

## Phase 4: User Story 2 - View/List All Tasks (P1)

**Goal**: Enable users to view all their tasks with clear status indicators per spec.md

**Independent Test**: Can be fully tested by viewing the task list after adding tasks, delivering visibility into the user's todo items per spec.md

**Tests**:
- [ ] T021 [P] [US2] Test that get_all_tasks returns all tasks
- [ ] T022 [P] [US2] Test that list command displays tasks in table format
- [ ] T023 [P] [US2] Test that status indicators are correctly shown

**Implementation**:
- [ ] T024 [US2] Implement list command in CLI interface using Rich Table per plan.md
- [ ] T025 [US2] Implement Rich table display with ID, Title, Description, Status columns per contracts/cli-api.md
- [ ] T026 [US2] Implement status indicators ([green]✓[/] for completed, [red]○[/] for pending) per plan.md

## Phase 5: User Story 3 - Mark Tasks as Complete/Incomplete (P2)

**Goal**: Enable users to mark tasks as complete or incomplete per spec.md

**Independent Test**: Can be fully tested by marking tasks as complete/incomplete and verifying the status changes in the list per spec.md

**Tests**:
- [ ] T027 [P] [US3] Test that mark_task_complete changes status to True
- [ ] T028 [P] [US3] Test that mark_task_incomplete changes status to False
- [ ] T029 [P] [US3] Test that marking non-existent task returns error

**Implementation**:
- [ ] T030 [US3] Implement mark_task_complete method in TaskManager per data-model.md
- [ ] T031 [US3] Implement mark_task_incomplete method in TaskManager per data-model.md
- [ ] T032 [US3] Implement complete command in CLI interface per contracts/cli-api.md
- [ ] T033 [US3] Implement incomplete command in CLI interface per contracts/cli-api.md
- [ ] T034 [US3] Implement CLI commands that call TaskManager methods per spec.md

## Phase 6: User Story 4 - Update Task Details (P2)

**Goal**: Enable users to update the title and description of their tasks per spec.md

**Independent Test**: Can be fully tested by updating task details and verifying the changes persist per spec.md

**Tests**:
- [ ] T035 [P] [US4] Test that update_task changes title correctly
- [ ] T036 [P] [US4] Test that update_task changes description correctly
- [ ] T037 [P] [US4] Test that updating non-existent task returns error

**Implementation**:
- [ ] T038 [US4] Implement update_task method in TaskManager with validation per data-model.md
- [ ] T039 [US4] Implement update command in CLI interface per contracts/cli-api.md
- [ ] T040 [US4] Implement CLI update command that calls TaskManager.update_task per spec.md

## Phase 7: User Story 5 - Delete Tasks by ID (P3)

**Goal**: Enable users to delete tasks they no longer need per spec.md

**Independent Test**: Can be fully tested by deleting tasks and verifying they no longer appear in the list per spec.md

**Tests**:
- [ ] T041 [P] [US5] Test that delete_task removes task from storage
- [ ] T042 [P] [US5] Test that deleting non-existent task returns error
- [ ] T043 [P] [US5] Test that deleted task no longer appears in list

**Implementation**:
- [ ] T044 [US5] Implement delete_task method in TaskManager per data-model.md
- [ ] T045 [US5] Implement delete command in CLI interface per contracts/cli-api.md
- [ ] T046 [US5] Implement CLI delete command that calls TaskManager.delete_task per spec.md

## Phase 8: CLI Interface and Main Application

- [ ] T047 Implement interactive command loop in CLI interface per plan.md
- [ ] T048 Implement help command in CLI interface per contracts/cli-api.md
- [ ] T049 Implement exit/quit command in CLI interface per contracts/cli-api.md
- [ ] T050 Implement error handling and validation in CLI per plan.md and spec.md
- [ ] T051 Implement consistent error message format per contracts/cli-api.md
- [ ] T052 Create main entry point that initializes TaskManager and starts CLI per plan.md

## Phase 9: Polish & Cross-Cutting Concerns

- [ ] T053 Add docstrings to all functions and classes per constitution.md
- [ ] T054 Add input validation throughout CLI interface per spec.md and contracts/cli-api.md
- [ ] T055 Add comprehensive error handling per spec.md and plan.md
- [ ] T056 Add user-friendly prompts and feedback per spec.md
- [ ] T057 Test all commands work together in integrated system
- [ ] T058 Add type hints to all functions per constitution.md
- [ ] T059 Verify all functional requirements from spec.md are implemented (FR-001 through FR-011)
- [ ] T060 Verify application meets success criteria from spec.md (SC-001 through SC-005)