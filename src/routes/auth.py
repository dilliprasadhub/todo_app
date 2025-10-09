from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from src.config.db import db

templates=Jinja2Templates(directory="templates")


router = APIRouter()

@router.get('/')
def home():
    return RedirectResponse('/login')


@router.get("/login")
def show_signup_page(request:Request):
    return templates.TemplateResponse("login.html",{"request":request})


@router.post("/login")
def singup_user(request:Request , email=Form(...),password=Form(...)):
    result=db.auth.sign_in_with_password({
        "email":email,
        "password":password
    })

    if result.session.access_token:
        response=RedirectResponse('/dashboard',status_code=303)
        response.set_cookie(key="user_session", value=result.session.access_token,max_age=3600)
        return response
   