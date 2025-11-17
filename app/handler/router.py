from fastapi import APIRouter

from app.handler.ping.ping import router as ping_router
from app.handler.task.create import router as create_router
from app.handler.task.read import router as read_router
from app.handler.task.update import router as update_router
from app.handler.task.delete import router as delete_router
from app.handler.user.create import router as register_router
from app.handler.user.login import router as login_router
from app.handler.task.createTaskWithUser import router as create_with_user_router
from app.handler.task.getAllTasks import router as read_all_with_user_router
from app.handler.task.getTaskByCategory import router as read_category_with_user_router
from app.handler.task.getTaskById import router as read_id_with_user_router
from app.handler.task.getTaskByTitle import router as read_title_with_user_router

api_router = APIRouter()
api_router.include_router(ping_router)
api_router.include_router(create_router)
api_router.include_router(read_router)
api_router.include_router(update_router)
api_router.include_router(delete_router)
api_router.include_router(register_router)
api_router.include_router(login_router)
api_router.include_router(create_with_user_router)
api_router.include_router(read_all_with_user_router)
api_router.include_router(read_category_with_user_router)
api_router.include_router(read_id_with_user_router)
api_router.include_router(read_title_with_user_router)
