from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
#import model

app = FastAPI(
    title="CodeSummarization"
)

# Jinja2 templates configuration
templates = Jinja2Templates(directory="templates")

# initialize model

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}

@app.post("/", response_class=HTMLResponse)
async def process_form(request: Request, code: str = Form(...)):
    # Make prediction using your model
    result_summary = "mock code summarization"  # Replace with your actual prediction function

    return templates.TemplateResponse("result.html", {"request": request, "code": code, "result_summary": result_summary})

## from fastapi import FastAPI, Request, Form

