def add_task(data: dict, task: str):
    data["tasks"].append({"id": len(data["tasks"]) + 1, "name": task, "status": "todo"})


def update_task(data: dict, i: int, t: str):
    data["tasks"][i - 1]["name"] = t

def pop_task(data: dict, i:int):
    return data["tasks"].pop(i - 1)

def edit_status(data: dict,i:int, status: str):
    data["tasks"][i - 1]["status"] = status
