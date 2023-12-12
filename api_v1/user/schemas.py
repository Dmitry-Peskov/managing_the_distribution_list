from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    fullname: str
    group: str
    email: EmailStr
    isCurrentEmployee: bool
    isEnabled: bool


class UserGET(UserBase):
    id: int


class UserCREATE(BaseModel):
    pass
