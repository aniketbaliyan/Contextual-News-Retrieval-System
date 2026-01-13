from fastapi import Request
from fastapi.responses import JSONResponse
from psycopg2 import OperationalError

def register_exception_handlers(app):

    @app.exception_handler(ValueError)
    async def bad_request(request: Request, exc: ValueError):
        return JSONResponse(
            status_code=400,
            content={"error": "BadRequest", "detail": str(exc)}
        )

    @app.exception_handler(OperationalError)
    async def db_down(request: Request, exc: OperationalError):
        return JSONResponse(
            status_code=503,
            content={"error": "DatabaseUnavailable", "detail": "Database is down"}
        )

    @app.exception_handler(Exception)
    async def server_error(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"error": "InternalError", "detail": "Unexpected server error"}
        )
