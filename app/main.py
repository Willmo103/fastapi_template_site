from fastapi import FastAPI, Depends, Request
from fastapi.templating import Jinja2Templates

from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from pathlib import Path
from app.routers import user, auth

BASE_PATH = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_PATH / "templates"))
static_files = Path.joinpath(BASE_PATH, "templates", "static")

app = FastAPI()
app.mount("/static", StaticFiles(directory=static_files), name="static")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(auth.router)
