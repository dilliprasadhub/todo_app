from fastapi import FastAPI

from src.routes.tasks import router as tasks_route
from src.routes.auth import router as auth_router




app=FastAPI(title="Todo App")

app.include_router(tasks_route)
app.include_router(auth_router)