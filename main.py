"""
main.py
=======
Application Entry Point for AI-NIDS

WHY THIS FILE EXISTS:
    This is the main entry point to run the application. It configures
    logging, instantiates the FastAPI app via the factory, and configures
    the Uvicorn server for running the app. 

HOW TO RUN:
    python main.py
    # or
    uvicorn main:app --reload
"""

import sys
from pathlib import Path

# Ensure the app directory is in the Python path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.api.app_factory import create_app
from config.logging_config import setup_logging_from_settings, get_logger
from config.settings import get_settings, PROJECT_ROOT

# 1. Setup logging FIRST
setup_logging_from_settings()
logger = get_logger(__name__)

# 2. Get settings
settings = get_settings()

# 3. Create FastAPI app
app = create_app()

# 4. Setup Jinja2 templates for the dashboard
templates_dir = PROJECT_ROOT / "frontend" / "templates"
if not templates_dir.exists():
    templates_dir.mkdir(parents=True, exist_ok=True)

templates = Jinja2Templates(directory=str(templates_dir))

# Serve the dashboard at the root URL
@app.get("/", response_class=HTMLResponse, tags=["Dashboard"])
async def dashboard(request: Request):
    """
    Serve the main AI-NIDS dashboard UI.
    """
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "app_version": settings.app_version}
    )

if __name__ == "__main__":
    import uvicorn
    
    logger.info("Starting AI-NIDS Uvicorn server on %s:%d", settings.host, settings.port)
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        workers=settings.workers,
        reload=settings.reload,
        log_level=settings.log_level.lower(),
    )
