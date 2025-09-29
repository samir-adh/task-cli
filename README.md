# task-cli : A small todo list app in the terminal

## Installation

Start by cloning this repository :

```bash
# with ssh
git clone git@github.com:samir-adh/leetcode.git
# with http
git clone https://github.com/samir-adh/leetcode.git
```


Then run the following commands

```bash
pip install click
pip install -e .
```
and you're all set !

## Usage

### Add, update and delete tasks

#### Add a task to your list

```bash
task-cli add <your_task>
```

This will create a new task asign it an id, set its status to 'todo' and add it to your list.

#### update a task to your list

```bash
task-cli Update <task_id> <content>
```

This will update the task with corresponding to the id with the provided content.

#### Delete a task to your list

```bash
task-cli delete <task_id>
```

This will delete the task with the corresponding id.

### List tasks

You can list all your tasks by running :

```bash
task-cli list
```

Or you can filter them by status this way :

```bash
task-cli list <status>
```
The status can be : 'todo', 'in-progress' or 'done'

