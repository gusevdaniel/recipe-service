import uvicorn
from fastapi import FastAPI
from db.base import database
from endpoints import users, auth, recipes, admin

app = FastAPI(title="Recipe service")
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(recipes.router, prefix="/recipes", tags=["recipes"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True)
