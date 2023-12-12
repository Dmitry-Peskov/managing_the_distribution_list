from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):
    fullname: str
    group: str
    email: EmailStr
    isCurrentEmployee: bool
    isEnabled: bool


class UserGET(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class UserCREATE(UserBase):
    pass
