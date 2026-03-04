from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from models import Base
from routers.vendas import router as vendas_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vendeu Amor API")  

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(vendas_router)

@app.get("/")
def root():
    return {"status": "Sistema Vendeu Amor Online"}