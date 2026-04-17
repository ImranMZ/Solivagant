"""
ASGI config for PythonAnywhere deployment.
"""
import os
from pathlib import Path

# Add the current directory to Python path
os.chdir(str(Path(__file__).parent.parent))

# Manual environment loading for PythonAnywhere
from dotenv import load_dotenv
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=str(env_path))

# Import the FastAPI app
from app.main import app as application

app = application