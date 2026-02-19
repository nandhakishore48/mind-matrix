import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from database import engine, Base
from routes import auth_routes, brand_routes, content_routes, sentiment_routes, chat_routes, project_routes, admin_routes

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BrandCraft API",
    description="AI-Powered Branding Automation System",
    version="1.0.0"
)

# CORS — allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500", "http://127.0.0.1:8000", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_routes.router)
app.include_router(brand_routes.router)
app.include_router(content_routes.router)
app.include_router(sentiment_routes.router)
app.include_router(chat_routes.router)
app.include_router(project_routes.router)
app.include_router(admin_routes.router)


@app.get("/")
def root():
    return {
        "name": "BrandCraft API",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


# Serve frontend
frontend_dir = os.path.join(os.path.dirname(__file__), "..", "frontend")
if os.path.exists(frontend_dir):
    app.mount("/css", StaticFiles(directory=os.path.join(frontend_dir, "css")), name="css")
    app.mount("/js", StaticFiles(directory=os.path.join(frontend_dir, "js")), name="js")

    @app.get("/{page}.html")
    def serve_page(page: str):
        file_path = os.path.join(frontend_dir, f"{page}.html")
        if os.path.exists(file_path):
            return FileResponse(file_path, media_type="text/html")
        return FileResponse(os.path.join(frontend_dir, "index.html"), media_type="text/html")

    @app.get("/app")
    def serve_index():
        return FileResponse(os.path.join(frontend_dir, "index.html"), media_type="text/html")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
