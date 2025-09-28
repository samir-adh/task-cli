import click
import json


@click.group()
def task_cli():
    # click.echo(f"Welcome {os.getlogin()} !")
    pass


@task_cli.command("add")
@click.argument("t", type=click.STRING)
def add(t: str):
    with open("tasks.json", "r+") as file:
        data = json.load(file)
        data["tasks"].append(
            {"id": len(data["tasks"]) + 1, "name": t, "status": "todo"}
        )

        file.seek(0)
        file.truncate()

        json.dump(data, file, indent=4)
        click.echo(f"Successfully added task : '{t}'")


@task_cli.command("update")
@click.argument("id", type=click.INT)
@click.argument("t", type=click.STRING)
def update(id: int, t: str):
    with open("tasks.json", "r+") as file:
        data = json.load(file)
        data["tasks"][id - 1]["name"] = t

        file.seek(0)
        file.truncate()

        json.dump(data, file, indent=4)
        click.echo(f"Successfully updated task {id} : '{t}'")


@task_cli.command("delete")
@click.argument("id", type=click.INT)
# @click.argument("t", type=click.STRING)
def delete(id: int):
    with open("tasks.json", "r+") as file:
        data = json.load(file)
        t = data["tasks"][id - 1]["name"]
        data["tasks"].pop(id - 1)

        file.seek(0)
        file.truncate()

        json.dump(data, file, indent=4)
        click.echo(f"Successfully deleted task {id} : '{t}'")


@task_cli.command("mark-in-progress")
@click.argument("id", type=click.INT)
def mark_in_progress(id: int):
    with open("tasks.json", "r+") as file:
        data = json.load(file)
        data["tasks"][id - 1]["status"] = "in progress"

        file.seek(0)
        file.truncate()

        json.dump(data, file, indent=4)
        click.echo(f"Task {id} is now in progress")


@task_cli.command("mark-done")
@click.argument("id", type=click.INT)
def mark_done(id: int):
    with open("tasks.json", "r+") as file:
        data = json.load(file)
        data["tasks"][id - 1]["status"] = "in progress"

        file.seek(0)
        file.truncate()

        json.dump(data, file, indent=4)
        click.echo(f"Task {id} is done!")


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
