from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.server import router

app = FastAPI(title="ChatKit Starter API")

# Enable CORS (for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes from server.py
app.include_router(router)