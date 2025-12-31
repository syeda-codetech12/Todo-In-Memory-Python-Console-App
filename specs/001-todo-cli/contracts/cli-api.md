# CLI API Contract: Todo CLI Application

## Overview

This document defines the API contract for the Todo CLI application, specifying the commands, inputs, outputs, and error handling.

## Commands

### Add Task
- **Command**: `add`
- **Input**: `add <title> [-d <description>]`
- **Success Response**:
  - Message: "Task added successfully with ID: {id}"
  - Status: Success
- **Error Response**:
  - Message: "Error: Title cannot be empty"
  - Status: Error

### List Tasks
- **Command**: `list`
- **Input**: `list`
- **Success Response**:
  - Output: Table with columns [ID, Title, Description, Status]
  - Status: Success
- **Error Response**: N/A

### Update Task
- **Command**: `update`
- **Input**: `update <id> <new_title> [-d <new_description>]`
- **Success Response**:
  - Message: "Task {id} updated successfully"
  - Status: Success
- **Error Response**:
  - Message: "Error: Task with ID {id} not found"
  - Status: Error

### Delete Task
- **Command**: `delete`
- **Input**: `delete <id>`
- **Success Response**:
  - Message: "Task {id} deleted successfully"
  - Status: Success
- **Error Response**:
  - Message: "Error: Task with ID {id} not found"
  - Status: Error

### Complete Task
- **Command**: `complete`
- **Input**: `complete <id>`
- **Success Response**:
  - Message: "Task {id} marked as complete"
  - Status: Success
- **Error Response**:
  - Message: "Error: Task with ID {id} not found"
  - Status: Error

### Incomplete Task
- **Command**: `incomplete`
- **Input**: `incomplete <id>`
- **Success Response**:
  - Message: "Task {id} marked as incomplete"
  - Status: Success
- **Error Response**:
  - Message: "Error: Task with ID {id} not found"
  - Status: Error

### Help
- **Command**: `help`
- **Input**: `help`
- **Success Response**:
  - Output: List of available commands with descriptions
  - Status: Success

### Exit
- **Command**: `exit` or `quit`
- **Input**: `exit` or `quit`
- **Success Response**:
  - Message: "Goodbye!"
  - Status: Exit application

## Error Handling

All commands follow a consistent error response pattern:
- Format: "Error: {descriptive message}"
- Exit code: Non-zero for errors

## Validation Rules

- Task ID must be a positive integer
- Task title cannot be empty
- Task ID must exist in the system for update/delete/complete operations