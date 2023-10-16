import os

import uvicorn
from job_searcher.app import app

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=8000), log_level="info")
