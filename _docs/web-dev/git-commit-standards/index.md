---
parent: Web Dev
layout: default
title: Git Commit Standards
date: Oct 26, 2024
excerpt: Git Commit Standards (Official)
permalink: git -commit-standards
---

git cheat sheet: https://media.licdn.com/dms/image/v2/D4D22AQFWkWeD6D4ksA/feedshare-shrink_1280/feedshare-shrink_1280/0/1729225766763?e=1732147200&v=beta&t=lRJJDZeffcMU0rbvRJi0oSef2p3xGOG9BQWXG9dhrTQ

### Example Commit Message

```
feat(task-manager): add task sorting feature

Implement a new feature that allows users to sort tasks by their deadlines. This improvement enhances user experience by enabling better task management.
```

### Breakdown of the Commit Message

1. **Type**: 
   - `feat`: This indicates that a new feature has been added to the project.

2. **Scope**: 
   - `(task-manager)`: This specifies the part of the codebase that the change affects, which is the task manager component.

3. **Description**: 
   - `add task sorting feature`: A brief summary of what was done. It’s clear and to the point.

4. **Body** (optional):
   - The body provides additional context about the change. Here, it describes what the new feature does and its benefits.

### Other Examples

#### Bug Fix
```
fix(task-table): resolve table sorting bug

Fix an issue where tasks were not sorting correctly when the user clicked the header. This resolves discrepancies in the task display order.
```

#### Documentation Update
```
docs: update README with setup instructions

Revise the README to include step-by-step setup instructions for new contributors, improving accessibility to the project.
```

#### Style Change
```
style(TaskModal): adjust button alignment

Change the alignment of the buttons in the TaskModal component to improve the visual layout without affecting functionality.
```

#### Refactor
```
refactor(file-upload): simplify file validation logic

Refactor the file validation logic in the FileUpload component to make it more readable and maintainable without changing the behavior.
```

#### Test Addition
```
test(task-service): add unit tests for createTask function

Add unit tests for the createTask function to ensure that it handles various input scenarios correctly.
```

#### Chore
```
chore: update dependencies

Update project dependencies to their latest versions to improve security and performance.
```

### Summary
By following this structured format, your commit messages become more informative and standardized, making it easier for collaborators and contributors to understand the changes made to the codebase.
