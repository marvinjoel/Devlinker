from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from controllers.auth import authRouter
from controllers.profile import profile

app = FastAPI()

app.include_router(authRouter)
app.include_router(profile)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)