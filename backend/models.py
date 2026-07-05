from pydantic import BaseModel

class ProductRequest(BaseModel):
    webpage: str
    question: str

class ProductResponse(BaseModel):
    answer: str


