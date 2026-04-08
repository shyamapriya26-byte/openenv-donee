import sys
import os
import uvicorn

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def main():
    """Entry point for OpenEnv validator"""
    uvicorn.run("app:app", host="0.0.0.0", port=int(os.environ.get("PORT", 7860)))

if __name__ == "__main__":
    main()
