from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)


class Permission(BaseModel):
    name: str
    reg_no: str
    permission_type: str
    reason: str
    day: int
    month: int
    year: int
    destination: str


permissions = []
permissions_id = {}


@app.post("/permission")
async def create_permission(permission: Permission):
    permissions.append(permission)
    id = len(permissions)

    permission_data = permission.model_dump()

    permission_data["id"] = id

    return permission_data
