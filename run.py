# run.py
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'web_app'))

if __name__ == "__main__":
    import uvicorn
    # Правильный формат для reload
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)