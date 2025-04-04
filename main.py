from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routers import survey
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
origins = [
    "http://localhost",  # Vite React 開發環境
    "http://127.0.0.1",  # 有時瀏覽器會用 127.0.0.1
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],             # 可允許的來源
    allow_credentials=True,           # 是否允許攜帶 cookie
    allow_methods=["*"],              # 允許所有 HTTP 方法 (GET, POST, PUT, DELETE...)
    allow_headers=["*"],              # 允許所有 headers
)

# 設定前端目錄
FRONTEND_DIST_PATH = r"C:\Users\{user_name}\Desktop\Programming\heart_key_website_fe\dist"
if not os.path.exists(FRONTEND_DIST_PATH):
    raise RuntimeError(f"Directory '{FRONTEND_DIST_PATH}' does not exist")

# Serve React build static files
app.mount("/assets", StaticFiles(directory=os.path.join(FRONTEND_DIST_PATH, "assets")), name="assets")
app.include_router(router=survey.router,prefix="/api/survey")
# Define the structure of the survey data
class SurveyData(BaseModel):
    name: str
    age: str

# Serve the React index.html page (this will be your frontend)
@app.get("/")
async def serve_index():
    return FileResponse(os.path.join(FRONTEND_DIST_PATH, "index.html"))

# POST endpoint to receive survey data
@app.post("/api/submit")
async def submit_survey(data: SurveyData):
    # Process the survey data here (e.g., save to a database, print, etc.)
    print("Received Survey Data:", data)
    return {"status": "success", "data": data.model_dump()}

