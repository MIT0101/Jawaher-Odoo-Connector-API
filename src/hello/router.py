from fastapi import APIRouter, Query, Depends
from odoo.api import Environment

from src.odoo_integration.providers import get_sudo_env

router = APIRouter()


@router.get("/world",
            tags=["hello"],
            summary="Get a greeting message",
            response_description="A greeting message")
async def get_hello_world(odoo_env: Environment = Depends(get_sudo_env)):
    p = odoo_env['res.partner'].search([], limit=1)
    return {
        "name": p.name if p else None,
        "message": "Hello, World! , with first partner name"
    }
