from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.errors import NotFoundError, ConflictError


def app_exception_handler(_request: Request, _exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )


def not_found_handler(_request: Request, exc: NotFoundError):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc)}
    )


def conflict_handler(_request: Request, exc: ConflictError):
    return JSONResponse(
        status_code=409,
        content={"detail": str(exc)}
    )