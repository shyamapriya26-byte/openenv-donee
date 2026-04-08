# This just imports your existing FastAPI app and re-exports it
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app

# The OpenEnv validator will look for this
