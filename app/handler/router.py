from fastapi import APIRouter

from app.handler.ping.ping import router as ping_router
from app.handler.task.create import router as create_router
from app.handler.task.read import router as read_router
from app.handler.task.update import router as update_router
from app.handler.task.delete import router as delete_router
from app.handler.user.create import router as register_router
from app.handler.user.login import router as login_router

api_router = APIRouter()
api_router.include_router(ping_router)
api_router.include_router(create_router)
api_router.include_router(read_router)
api_router.include_router(update_router)
api_router.include_router(delete_router)
api_router.include_router(register_router)
api_router.include_router(login_router)
