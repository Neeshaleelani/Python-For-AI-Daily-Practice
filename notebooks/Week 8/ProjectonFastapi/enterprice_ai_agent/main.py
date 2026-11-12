from fastapi import FastAPI
# import new router we made
from modules.ai_agent.router import ai_agent_router

app = FastAPI()
app.include_router(
    ai_agent_router,
    tags=["AI module"]
)


@app.get("/",status_code=200)
async def root():
    return {"Hello": "You are at the Xender's API"}


# @app.get("/")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}