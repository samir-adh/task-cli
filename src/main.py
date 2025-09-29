import click
import json
import os

from commands import add_task, edit_status, pop_task, update_task


@click.group(invoke_without_command=True)
@click.pass_context
def task_cli(ctx: click.Context):
    if ctx.invoked_subcommand is None:
        click.echo(f"Welcome {os.getlogin()} !")


@task_cli.command("add", help="Adds a task to the list.")
@click.argument("t", type=click.STRING)
def add(t: str):
    with open("tasks.json", "r+") as file:
        data = json.load(file)
        add_task(data, t)

        file.seek(0)
        file.truncate()

        json.dump(data, file, indent=4)
        click.echo(f"Successfully added task : '{t}'")


@task_cli.command("update", help="Changes the content of a task.")
@click.argument("id", type=click.INT)
@click.argument("t", type=click.STRING)
def update(i: int, t: str):
    with open("tasks.json", "r+") as file:
        data = json.load(file)
        update_task(data, i, t)

        file.seek(0)
        file.truncate()

        json.dump(data, file, indent=4)
        click.echo(f"Successfully updated task {id} : '{t}'")


@task_cli.command("delete", help="Deletes a task from the list.")
@click.argument("id", type=click.INT)
# @click.argument("t", type=click.STRING)
def delete(i: int):
    with open("tasks.json", "r+") as file:
        data = json.load(file)

        t = pop_task(data, i)
        file.seek(0)
        file.truncate()

        json.dump(data, file, indent=4)
        click.echo(f"Successfully deleted task {i} : '{t['name']}'")


@task_cli.command("mark-in-progress", "Set the status of a task to 'in-progress'")
@click.argument("id", type=click.INT)
def mark_in_progress(i: int):
    with open("tasks.json", "r+") as file:
        data = json.load(file)
        edit_status(data, i, "in-progress")

        file.seek(0)
        file.truncate()

        json.dump(data, file, indent=4)
        click.echo(f"Task {i} is now in progress")


@task_cli.command("mark-done")
@click.argument("id", type=click.INT)
def mark_done(i: int):
    with open("tasks.json", "r+") as file:
        data = json.load(file)
        edit_status(data, i, "done")

        file.seek(0)
        file.truncate()

        json.dump(data, file, indent=4)
        click.echo(f"Task {i} is done!")


@task_cli.command("list")
@click.argument("status", type=click.STRING, default="all")
def list(status: str):
    with open("tasks.json", "r") as file:
        data = json.load(file)
        tasks = data["tasks"]
        for task in tasks:
            if status == "all" or task["status"] == status:
                click.echo(f"{task['id']} - {task['name']} : {task['status']}")


if __name__ == "__main__":
    task_cli()
