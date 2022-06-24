from .worker import create_task
from fastapi import APIRouter

router = APIRouter(
    prefix="/task",
    tags=["task"]
)

@router.post("/{time}", status_code=201)
def run_task(time: int):
    task = create_task.delay(time)
    return {"task_id": task.id}