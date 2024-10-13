
# Personal To-Do List Application

## Overview
This is a simple command-line-based To-Do List Application that allows users to create, view, complete, and delete tasks. Tasks are categorized and stored in a JSON file for persistence.

## Features
- **Add Tasks**: Create tasks with a title, description, and category.
- **View Tasks**: Display all tasks with their status (Pending/Completed).
- **Mark Completed**: Mark tasks as completed.
- **Delete Tasks**: Remove tasks from the list.
- **Persistent Storage**: Tasks are saved to a JSON file between sessions.

## How to Run
1. Ensure Python 3.x is installed on your machine.
2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/personal-todo-list.git
   ```
3. Navigate into the project directory:
   ```bash
   cd personal-todo-list
   ```
4. Run the application:
   ```bash
   python todo.py
   ```

## Project Structure
```
/personal-todo-list
 ├── todo.py        # Main application logic
 ├── tasks.json     # Task storage file
 └── README.md      # Documentation
```

## Usage
- Follow the prompts in the terminal to add, view, complete, or delete tasks.
- Tasks are saved automatically when exiting the program.

## License
This project is free to use and modify.
