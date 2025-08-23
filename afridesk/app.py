# Main application file for AfriDesk backend services

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "AfriDesk API is running"}

# Import and include routers
# from .routers import users, clinics, services
# app.include_router(users.router)
# app.include_router(clinics.router)
# app.include_router(services.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
