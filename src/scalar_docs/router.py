from fastapi import APIRouter
from scalar_fastapi import get_scalar_api_reference

scalar_docs_router = APIRouter()


@scalar_docs_router.get("/scalar_docs", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )
