from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware


def make_middleware() -> list[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
    ]
    return middleware


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Kokoro Be",
        description="Kokoro Be",
        version="1.0.0",
        middleware=make_middleware(),
    )

    return app_


app = create_app()
