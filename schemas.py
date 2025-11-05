from pydantic import BaseModel, Field,   EmailStr


class UserRequest(BaseModel):
    name: str | None = Field(
        default=None, title="The name", min_length=3, max_length=100
    )
    email: EmailStr = Field(..., description="User email address")
    age: int = Field(..., ge=0, le=120, description="User age (0-120)")
    password: str = Field(..., min_length=8, max_length=50, description="Password must be 8-50 characters long")