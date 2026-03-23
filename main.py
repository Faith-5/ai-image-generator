import os
import uuid
import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel
from services.image_services import generate_image_service
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title= 'Ultra - AI Image Generator',
    version= '1.0.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

IMAGE_DIR = "static/images"
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")

template = Jinja2Templates(directory="template")

class ImageRequest(BaseModel):
    prompt: str
    model: str = "flux"

@app.get('/')
def root(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@app.post('/generate')
def generate_image(request: ImageRequest):
    filename = os.path.join(IMAGE_DIR, f"{uuid.uuid4()}.jpg")
    image_url = generate_image_service(request.prompt, request.model, filename)
    if image_url:
        image_url = f"/{image_url.replace(os.sep, '/')}"
        return {"image_url": image_url}
    else:
        return {"error": "Failed to generate image."}
    
@app.get('/download')
def download_image(file_path: str):
    local_path = file_path.strip("/")
    if os.path.exists(local_path):
        return FileResponse(local_path, media_type="image/jpeg", filename='image.jpg')
    return {"error": "Image not found."}

    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=os.environ.get("PORT", 8000))