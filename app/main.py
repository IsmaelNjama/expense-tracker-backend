
"""FastAPI application initialization and configuration"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.config import CORS_ORIGINS
from .api.routes import friends, expenses, summary
from .core.storage import storage


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    print("Application startup!")
    storage.load()
    yield
    # Shutdown logic
    print("Application shutdown!")


def create_app() -> FastAPI:
    """Create and configure FastAPI application"""
    app = FastAPI(
        title="Cost Tracker API",
        description="API for managing expenses and tracking costs among friends",
        version="1.0.0",
        lifespan=lifespan,
    )

    # Enable CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_ORIGINS,  # Vite default port
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include API routes
    app.include_router(friends.router)
    app.include_router(expenses.router)
    app.include_router(summary.router)

    return app


app = create_app()


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Cost Tracker API", "status": "running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
