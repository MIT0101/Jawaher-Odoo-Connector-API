from fastapi import Depends, FastAPI, APIRouter

from src.odoo_integration.utils import initialize_odoo
from src.hello.router import router as hello_router

# Initialize Odoo when the application starts
initialize_odoo()

app = FastAPI(
    title="Odoo Connect API",
    description="API for Odoo integration",
    version="1.0.0",
)
## Hello world router
app.include_router(hello_router, prefix="/hello")
