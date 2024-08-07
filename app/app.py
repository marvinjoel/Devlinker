from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from controllers.auth import authRouter

app = FastAPI()

app.include_router(authRouter)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)