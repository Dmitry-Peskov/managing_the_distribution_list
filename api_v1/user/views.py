from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud
from .schemas import UserGET, UserCREATE
from core.models.db_helper import db_helper

router = APIRouter(tags=["Users"])


@router.post("/", response_model=UserGET)
async def createUser(
        new_user: UserCREATE,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.create_user(session=session, new_user=new_user)


@router.get("/", response_model=list[UserGET])
async def getUsers(
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.get_users(session=session)


@router.get("/{user_id}/", response_model=UserGET)
async def getUser(
        user_id: int,
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    user = await crud.get_user(session=session, user_id=user_id)
    if user is not None:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Пользователь с ID={user_id} не найдет в системе"
    )
