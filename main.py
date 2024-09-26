from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()

# 정적 파일 경로 설정
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 템플릿 경로 설정
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def get_resume(request: Request):
    return templates.TemplateResponse("resume.html", {"request": request})

