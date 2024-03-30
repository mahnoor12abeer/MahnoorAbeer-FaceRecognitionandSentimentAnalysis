from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import StreamingResponse
from werkzeug.utils import secure_filename
from app.face_and_emotion_detection import gen_frames
import os
from shutil import copyfileobj
from tempfile import NamedTemporaryFile
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

app.secret_key = 'your_secret_key'  # FastAPI uses different ways to manage secrets
upload_folder = 'app/uploads'
allowed_extensions = {'mp4', 'avi', 'mov'}

# For simplicity, using in-memory storage; consider changing for large files or production
uploaded_file_path = None

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.get("/", response_class=HTMLResponse)
async def upload_file(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)):
    global uploaded_file_path
    if file.filename == '':
        raise HTTPException(status_code=400, detail="No selected file")
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(upload_folder, filename)
        with NamedTemporaryFile(delete=False, dir=upload_folder) as tmp:
            copyfileobj(file.file, tmp)
            tmp_file_name = tmp.name
        uploaded_file_path = tmp_file_name  # Assign the temp file name to be globally accessible
        return templates.TemplateResponse("index.html", {"request": request})
    return templates.TemplateResponse("upload.html", {"request": request})

@app.get("/stream", response_class=HTMLResponse)
async def stream_video(request: Request):
    global uploaded_file_path
    if uploaded_file_path:
        return templates.TemplateResponse("index.html", {"request": request})
    else:
        raise HTTPException(status_code=400, detail="No file uploaded")

@app.get("/video_feed")
async def video_feed():
    if uploaded_file_path:
        # We need a streaming response frame generator
        return StreamingResponse(gen_frames(uploaded_file_path), media_type='multipart/x-mixed-replace; boundary=frame')
    else:
        raise HTTPException(status_code=400, detail="No file uploaded")

@app.get("/stop")
async def stop():
    return JSONResponse({"message": "Server will shut down..."})