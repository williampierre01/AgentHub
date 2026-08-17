from fastapi import FastAPI


app = FastAPI(title="AgentHub", version="0.1.0")


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "AgentHub API"}
