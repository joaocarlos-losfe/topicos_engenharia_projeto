from fastapi import FastAPI
from routers import user, auth

app = FastAPI();

app.include_router(user.router);
app.include_router(auth.router);

@app.get("/")
async def root():
    return "microserviço de usuário está ativo 🚀"