from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 정적 파일 마운트
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_resume(request: Request):
    return templates.TemplateResponse("resume.html", {"request": request})
