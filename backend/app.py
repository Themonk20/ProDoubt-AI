from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rag import ask_product
from models import ProductResponse, ProductRequest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():

    return {
        "message": "Welcome to ProDoubt Backend"
    }


@app.get("/health")
def health():

    return {
        "status": "running"
    }


@app.post("/ask", response_model=ProductResponse)
def ask(request: ProductRequest):

    answer = ask_product(
        question=request.question,
        webpage=request.webpage
    )

    return ProductResponse(
        answer=answer
    )
    
    

