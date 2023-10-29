from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from controllers.UserController import user_controller_router
from controllers.TextController import text_controller_router
from controllers.PromptManagerController import prompt_manager_controller_router
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

tags_metadata = [
    {"name": "Users", "description": "Operations related to user management"},
    {"name": "Text", "description": "Operations related to text management"},
    {"name": "Prompt Manager", "description": "Operations related to prompt management."}
]

# Include the routers from controller modules
app.include_router(user_controller_router, prefix="/users", tags=["Users"])
app.include_router(text_controller_router, prefix="/texts", tags=["Text"])
app.include_router(prompt_manager_controller_router, prefix="/prompt_manager", tags=["Prompt Manager"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run("app:app",host=os.environ.get("HOST"), port=int(os.environ.get("PORT")), reload=True)