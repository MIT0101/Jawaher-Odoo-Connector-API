from src.odoo_integration.utils import initialize_odoo

# Initialize Odoo when the application starts
initialize_odoo()

from fastapi import Depends, FastAPI, APIRouter

from src.hello.router import router as hello_router
from src.auth.router import auth_router

app = FastAPI(
    title="Odoo Connector API",
    description="API for Odoo integration",
    version="1.0.0",
)
app_router = APIRouter(prefix="/api/v1")
## Hello world router
# app_router.include_router(hello_router, prefix="/hello")

## Auth router
app_router.include_router(auth_router, prefix="/auth")

app.include_router(app_router)
