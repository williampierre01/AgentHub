from fastapi import FastAPI, status


app = FastAPI(title="AgentHub", version="0.1.0")


@app.get("/", tags=["general"], summary="Exibe a mensagem inicial")
async def read_root() -> dict[str, str]:
    return {"message": "AgentHub API"}


@app.get(
    "/health",
    tags=["health"],
    summary="Verifica a disponibilidade da API",
    status_code=status.HTTP_200_OK,
)
async def read_health() -> dict[str, str]:
    return {"status": "ok"}
