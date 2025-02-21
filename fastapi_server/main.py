from fastapi import FastAPI
from routers import data_router, users_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to restrict origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


app.include_router(data_router)
app.include_router(users_router)

app.get('/')
def is_runnig():
    return True


if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8000, reload=True )